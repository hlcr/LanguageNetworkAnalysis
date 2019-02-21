# encoding=utf-8
import string

import jieba
import re
import util


# 过滤微博中的无用字符
def input_filer(temp):
    # 匹配url
    temp = re.sub("(分享自@\S+)", '', temp)
    temp = re.sub("(@\S+)", '', temp)
    # 将正则表达式编译成Pattern对象
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
    match = pattern.findall(temp)
    return ' '.join(match)

rr_list = [];

with open('2013-02-03.txt','r',encoding='utf-8') as r_file:
    r_list = r_file.readlines()
    for sentence in r_list:
        sentence = sentence.strip().rstrip('\n')
        if sentence is not None and sentence != '':
            rr_list.append(input_filer(sentence))

util.save_file('result.txt',rr_list)

# jieba.load_userdict("D:\semantic analysis\分词\词库\导出结果\dict1.txt")
# jieba.set_dictionary("D:\semantic analysis\分词\词库\导出结果\dict1.txt")
# jieba.initialize()
# seg_list = jieba.cut(test_str, cut_all=False)

# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# print(" ".join(seg_list))