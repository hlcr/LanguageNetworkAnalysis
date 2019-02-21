# 从每个xml中随机抽取一句话，用于展示
import os
import xml.etree.ElementTree as ET
import random


def randomly_extract(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    contents = root.findall(".//content")
    times = root.findall(".//time")

    sum_num = len(contents)
    index = random.randint(0,(sum_num-1))
    return contents[index].text,times[index].text


def randomly_extract_file(file_dir):
    if file_dir is not None:
        os.chdir(file_dir)
    currentFiles = os.listdir('./')
    xmlFiles = [xmlfile for xmlfile in currentFiles if '.xml' in xmlfile]
    contentlist = []
    for file_name in xmlFiles:
        c,t = randomly_extract(file_name)
        contentlist.append([c,t])

    with open('content.txt','w', encoding="utf-8") as content_file:
        for item in contentlist:
            content_file.write(str(item[0])+'\t'+str(item[1])+'\n')

randomly_extract_file('D://semantic analysis//2次采集//页面统计//test')

word_dict = {'人艰不拆':'人艱不拆','不明觉厉':'不明覺厲','扯淡':'扯淡','达人':'達人','淡定':'淡定','腹黑':'腹黑','纠结':'糾結','闷骚':'悶騷','山寨':'山寨','十动然拒':'十動然拒','完爆':'完爆'}
#os.chdir('D://semantic analysis//2次采集//页数统计')
for (k,v) in word_dict.items():
    print(k)
    randomly_extract_file('D://semantic analysis//2次采集//页面统计//'+k)