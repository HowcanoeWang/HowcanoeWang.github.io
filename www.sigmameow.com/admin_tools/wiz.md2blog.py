# -*- coding:utf-8 -*-
import os
import markdown
import zipfile
import datetime
import shutil
from bs4 import BeautifulSoup as BS
from bs4 import NavigableString
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askinteger
from tkinter.messagebox import askyesno


def convert(ziw_path, p_id, overwrite=False):
    to_folder = r'../blog/img/'
    html_dir = f'../blog/p/{p_id}.html'
    img_dir = os.path.join(to_folder, str(p_id))

    soup = read_ziw(ziw_path)
    md = soup2markdown(soup)

    md = md.replace('src="index_files', f'src="img/{p_id}')
    md = md.replace('[toc]', '\n[TOC]\n')
    md = md.replace('* ', '\n* ')

    md_ext = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'toc'])
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

    if overwrite:
        os.remove(html_dir)
        if os.path.exists(img_dir):
            shutil.rmtree(img_dir)
    else:  # add records to id.js file
        with open('../blog/id.js', 'r+', encoding='utf-8') as js:
            contents = js.read()
            id = p_id
            filename = ziw_path.split('/')[-1][:-7]
            modify_time = datetime.datetime.fromtimestamp(os.path.getmtime(ziw_path)).strftime("%Y.%m.%d")
            replace_word = f'}},\n{{"id":"{id}",\n"title":"{filename}",\n"subtitle":"",\n"author":"浩瀚猫",\n"word":"",\n' \
                f'"date":"{modify_time}",\n"img":"img/page-heading/xxx.jpg",\n"recommend":[]\n}}\n];'
            contents = contents.replace('}\n];', replace_word)
            js.seek(0)
            js.write(contents)

    extract_imgs(ziw_path, to_folder, p_id)
    outfile = open(html_dir, 'w', encoding="utf-8")
    outfile.write(html)
    outfile.close()

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

def extract_imgs(ziw_path, to_folder, p_id):
    zfile = zipfile.ZipFile(ziw_path, 'r')
    files = []
    for file in zfile.namelist():
        if file.startswith('index_files/'):
            files.append(file)
    if len(files) == 0:  # no imgs
        pass
    else:
        zfile.extractall(to_folder, members=files)
        os.rename(os.path.join(to_folder, 'index_files'),
                  os.path.join(to_folder, str(p_id)))
    zfile.close()


if __name__ == '__main__':
    root = Tk()
    root.withdraw()

    p_list = os.listdir('../blog/p/')

    wiz_path = os.path.normpath(os.path.expanduser(r'~/Documents/My Knowledge/Data'))
    ziw_path = askopenfilename(parent=root, initialdir=wiz_path, filetypes=[("ziw files", "*.ziw")])

    if os.path.isfile(ziw_path):
        loop = True
        while loop:
            p_id = askinteger(parent=root, title='La', prompt='Type this article id, currently have ' + str(p_list))
            if str(p_id)+'.html' in p_list:
                choice = askyesno(parent=root, title='Confirm', message='There is an exist id, overwrite?')
                if choice:
                    convert(ziw_path, p_id, overwrite=True)
                    loop=False
            else:
                convert(ziw_path, p_id)
                loop=False