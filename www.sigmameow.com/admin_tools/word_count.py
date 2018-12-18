# -*- coding: utf-8 -*-
import re
 
def strQ2B(ustring):
#字符串全角转半角
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:    #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring
 
def querySimpleProcess(ss):
#query预处理,排除中英文数字以外的字符，全部转为小写
    s1=strQ2B(ss)
    s2=re.sub(r"(?![\u4e00-\u9fa5]|[0-9a-zA-Z])."," ",s1) 
    s3=re.sub(r"\s+"," ",s2)
    return s3.strip().lower()
 
#判断是否包含中文
def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
 
#判断是否包含英文
def check_contain_english(check_str):
    for ch in check_str:
        if u'a' <= ch <= u'z' or u'A' <= ch <= u'Z':
            return True
    return False
 
#删除字符串中的英文字母，以便统计字符数之用
def delete_letters(ss):
    rs = re.sub(r"[a-zA-Z]+","",ss)
    return rs
 
#先行空格分割，得到列表，再行处理列表中的每个元素
#例：Smart校服广告曲=6、Disrespectful Breakup=2
#异常：C哩C哩=3 ###处理不了
#如果元素不包含中文，则该元素长度记为：1+数字个数
#如果元素不包含英文，则该元素长度记为：中文字符数+数字个数，可以直接使用len()方法
#如果元素同时包含中英文，则该元素长度记为：中文字符数+数字个数+1
def countCharacters(inputStr):
    tmpStr = querySimpleProcess(inputStr)
    str2list = tmpStr.strip().split(" ")
    if len(str2list) > 0:
        charsNum = 0#初始化字符计数
        for elem in str2list:
            chineseFlag = check_contain_chinese(elem)
            englishFlag = check_contain_english(elem)
            if englishFlag == False:#不包含英文
                charsNum = charsNum + len(elem)
                continue
            else:#包含英文
                elem = delete_letters(elem)
                charsNum = charsNum + 1 + len(elem)
        return charsNum
    return 0
