# -*- coding:utf-8 -*-
import os
import zipfile
import datetime
import shutil
import pickle
import time
import re
import markdown
from bs4 import BeautifulSoup as BS
from bs4 import NavigableString
from pandas import DataFrame, read_csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger
from tkinter.messagebox import askyesno, showinfo
from word_count import countCharacters


def add_new():
    id_list = [int(i[:-5]) for i in p_list]
    p_id = max(id_list) + 1   # next id

    if mode=='test':
        ziw_path = 'test.md.ziw'
    else:
        ziw_path = askopenfilename(parent=root, initialdir=wiz_path, filetypes=[("ziw files", "*.ziw")])

    if ziw_path is not None:
        word_count = ziw2html(ziw_path, p_id)

        extract_imgs(ziw_path, p_id)

        filename = ziw_path.split('/')[-1][:-4].split('.md')[0]
        modify_time = datetime.datetime.fromtimestamp(os.path.getmtime(ziw_path)).strftime("%Y.%m.%d")
        edit_js(p_id, filename, modify_time, word_count, way="add")

        # update pickle
        ziw_save_path = r"~/Documents/My Knowledge/Data" + ziw_path.split('/Documents/My Knowledge/Data')[-1]
        ref_df.loc[ref_df.index.max() + 1] = [p_id, filename, ziw_save_path]
        reference_dict(ref_df)
        showinfo(parent=root, title='Success', message='Convert Successfully')


def update_old():
    loop = True
    while loop:
        p_id = askinteger(parent=root, title='La',
                          prompt='Type Updated article id, currently have \n' + str(ref_df[['id','title']]))
        if p_id in ref_df['id'].values:
            loop = False
            search_df = ref_df.loc[ref_df['id'] == p_id]
            df_id = search_df.index[0]
            title = search_df['title'].values[0]
            ziw_path = os.path.normpath(os.path.expanduser(search_df['path'].values[0]))

            if not os.path.exists(ziw_path):
                showinfo(title='Error', message=f'Can not Find {title}, please redirect it!')
                ziw_path = askopenfilename(parent=root, title=f'Redirect [{title}]',
                                           initialdir=wiz_path, filetypes=[("ziw files", "*.ziw")])
                if ziw_path:
                    title = ziw_path.split('/')[-1][:-4].split('.md')[0]
                    ref_df.loc[df_id, 'title'] = title
                    ref_df.loc[df_id, 'path'] = ziw_path
                    reference_dict(ref_df)

            modify_time = datetime.datetime.fromtimestamp(os.path.getmtime(ziw_path)).strftime("%Y.%m.%d")
            word_count = ziw2html(ziw_path, p_id)
            extract_imgs(ziw_path, p_id)

            edit_js(p_id, title, modify_time, word_count, way="update")
            showinfo(parent=root, title='Success', message='Convert Successfully')

        else:
            showinfo(title='Opps', message='Only ' + str(ref_df['id'].values) + 'are supported!')



def ziw2html(ziw_path, p_id):
    soup = read_ziw(ziw_path)
    md = soup2markdown(soup)

    md = md.replace('src="index_files', f'src="img/{p_id}')
    md = md.replace(' ', ' ')    # wiz tab = '&nbsp;' + ' ' + '&nbsp;&nbsp;', what the fuck!!!!!!!!!!!!
    md = md.replace('[toc]', '\n[TOC]\n')
    md = replace_download_url(md, p_id)

    '''
    Add \n in the beginning and end of list block
    PyMarkdown only accept list dependent from other part (unlike wiz accept list connected from other sentence)
    [WizNote]          | [PyMarkdown]
    xxxxxxxxxxxxxx     | xxxxxxxxxxxxxxxxxxx
    1. xxx             |
    2. xxx             | 1. xxx
    3. xxx             | 2. xxx
    '''
    md_line = md.splitlines()
    md = ''
    in_list = False
    in_code = False
    black_line = False
    # re: 'a*' match 'a', 'aa', 'aaa', ...  $ to solve sublist '    1. ' problem
    # re: '\d' match all numbers 0-9
    # re: 'a{1,2}' match 'a' or 'aa'
    # re: '\.' match '.'
    # re: '\*' match '*'
    pattern = re.compile(r' *\d{1,2}\. | *\* ')  # find all '1. ' or '* ' which means list in markdown

    for l in md_line:
        if l == '':
            black_line = True
            continue
        else:
            if black_line:
                md += '\n'
                black_line = False
            # in code block
            if '```' in l:
                in_code = not in_code

            if in_code:
                md += f'{l}\n'
            else:
                contain_list = pattern.match(l) is not None
                # add two spaces in the end of a sentence, pymarkdown need two space to present a new line, but wiz note :)
                if contain_list and not in_list:
                    in_list = True
                    md += f'\n{l}  \n'
                elif contain_list and in_list:
                    md += f'{l}  \n'
                elif not contain_list and in_list:
                    # line start with four spaces means it is the sub contents of that list
                    if l[:4] == '    ':
                        md += f'{l}  \n'
                    else:
                        in_list = False
                        md += f'{l}  \n\n'
                else:   # common sentence
                    md += f'{l}  \n'

    extension_configs = {'mdx_math': {'enable_dollar_delimiter': True}}
    md_ext = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'toc', 'markdown_checklist.extension', 'mdx_math'],
                               extension_configs=extension_configs)
                               
    with open("test.txt", "w") as f:
        f.write(md)

    html = md_ext.convert(md)

    html = html.replace('<table>',
                        '<div class="table-responsive"><table class="table table-striped table-bordered" align="center">')
    html = html.replace('</table>', '</table></div>')
    html = html.replace('<h1', '<h1 class="section-heading text-center"')
    html = html.replace('<h3', '<h1 class="section-heading h3"')
    html = html.replace('<h5', '<h1 class="section-heading h5"')
    html = html.replace('<h6', '<h1 class="section-heading h6 text-muted"')
    html = html.replace('<blockquote', '<blockquote class="blockquote"')
    html = html.replace('<img', '<img class="img-fluid"')

    # write html
    if mode == 'test':
        html_dir = f'test/{p_id}.html'
    else:
        html_dir = f'../blog/p/{p_id}.html'
    outfile = open(html_dir, 'w', encoding="utf-8")
    outfile.write(html)
    outfile.close()

    # count word
    word= countCharacters(md)
    if  word < 1000:
        word_str = str(word)
    else:
        word_str = str(round(word / 1000,1)) + 'K'

    return word_str

def replace_download_url(md, p_id):
    # example:
    # >>> import re
    # >>> s = "the blue dog and blue cat wore blue hats"
    # >>> p = re.compile(r"blue (dog|cat)")
    # >>> p.sub('gray \\1',s)
    # 'the gray dog and gray cat wore blue hats'

    # replace <download>filename</download> to
    # <a href="https://www.sigmameow.com/blog/files/16/{filename}" download="{filename}">{filename}/a>
    pattern = re.compile(r'<download>(.*)</download>')
    urls = pattern.sub(f'<a href="https://www.sigmameow.com/blog/files/{p_id}/\\1" download="\\1">\\1</a>', md)

    return urls

def reference_dict(*args):
    if mode == 'test':
        csv_path = 'test/ref.csv'
    else:
        csv_path = 'ref.csv'
    if len(args) == 0:
        if os.path.exists(csv_path):
            ref = read_csv(csv_path)
        else:
            ref = DataFrame(columns=['id', 'title', 'path'])
            ref.to_csv(csv_path, index=False)
        return ref
    if len(args) == 1:
        args[0].to_csv(csv_path, index=False)


def edit_js(id, filename, modify_time, word_count, way="add"):
    now_time = datetime.datetime.now().strftime("%m.%d_%H.%M")
    if mode == 'test':
        shutil.copyfile('../blog/id.js', 'test/id.js')
        js_dir = 'test/id.js'
    else:
        shutil.copyfile('../blog/id.js', f'../blog/id_{now_time}.js')
        js_dir = '../blog/id.js'

    with open(js_dir, 'r+', encoding='utf-8') as js:
        if way == 'add':
            contents = js.read()
            replace_word = f'}},\n{{"id":"{id}",\n"title":"{filename}",\n"subtitle":"",\n"author":"浩瀚猫",\n"word":"{word_count}",\n' \
                f'"date":"{modify_time}",\n"img":"img/page-heading/blog-bg.jpg",\n"recommend":[]\n}}\n];'
            contents = contents.replace('}\n];', replace_word)
            js.seek(0)
            js.write(contents)
        else:  # update js
            contents = js.readlines()
            updated_contents = ''
            inline = -1
            for line in contents:
                if inline >= 0:
                    inline += 1
                # get into the part need to edit
                if f'"id":"{id}",' in line:
                    inline = 0

                if inline not in [1, 4, 5]:  # only edit line 1, 4, 5
                    updated_contents += line
                else:
                    if inline == 1:
                        updated_contents += f'"title":"{filename}",\n'
                    elif inline == 4:
                        updated_contents += f'"word":"{word_count}",\n'
                    elif inline == 5:
                        updated_contents += f'"date":"{modify_time}",\n'

            js.seek(0)
            js.write(updated_contents)


def read_ziw(ziw_path):
    zfile = zipfile.ZipFile(ziw_path, 'r')
    html = zfile.open('index.html')
    zfile.close()
    soup = BS(html.read(), "html5lib")
    
    # drop wiz unuseful tags
    for tag_rm in ['span', 'blockquote']:
        for match in soup.findAll(tag_rm):
            match.unwrap()

    for tag in soup():
        for attribute in ["class", "id", "name", "style", "align", "valign", "width", "height"]:
            del tag[attribute]

    return soup

def soup2markdown(soup):
    markdown_text = ''
    for child in soup.body.children:  # 遍历儿子节点
        if str(child) == "<div><br/></div>":
            child_text = '\n'
        else:
            child_text = contents_extract(child)
        markdown_text += child_text + '\n'

    return markdown_text

def contents_extract(tag):
    text = ''
    if tag.name == 'table':
        text += str(tag)
    elif tag.name == 'br':
        pass
    else:
        if len(tag.contents) == 0:
            text += str(tag)
        else:
            for t in tag.contents:
                if type(t) is NavigableString:
                    text += str(t)
                else:
                    text += contents_extract(t)
    return text

def extract_imgs(ziw_path, p_id):
    # clear old img_folder first
    if mode == 'test':
        to_folder = r'test/'
    else:
        to_folder = r'../blog/img/'
    img_dir = os.path.join(to_folder, str(p_id))
    if os.path.exists(img_dir):
        shutil.rmtree(img_dir)

    zfile = zipfile.ZipFile(ziw_path, 'r')
    files = []
    for file in zfile.namelist():
        if file.startswith('index_files/'):
            files.append(file)
    if len(files) == 0:  # no imgs
        pass
    else:
        zfile.extractall(to_folder, members=files)
        time.sleep(0.1)
        os.rename(os.path.join(to_folder, 'index_files'),
                  os.path.join(to_folder, str(p_id)))
    zfile.close()


if __name__ == '__main__':
    mode = 'test1'
    if mode == 'test':
        if os.path.exists('test'):
            shutil.rmtree('test')
        time.sleep(0.1)
        os.mkdir('test')
        if os.path.exists('ref.csv'):
            shutil.copyfile('ref.csv', 'test/ref.csv')

    root = Tk()
    root.withdraw()

    p_list = os.listdir('../blog/p/')
    p_list.remove('nan.html')

    wiz_path = os.path.normpath(os.path.expanduser(r'~/Documents/My Knowledge/Data'))
    ref_df = reference_dict()

    choice = askyesno(parent=root, title='Mode', message='Add new article [Y] or update old article [N]?')
    if choice:
        add_new()
    else:
        update_old()