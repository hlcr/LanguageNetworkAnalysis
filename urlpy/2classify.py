# 通过移动文件达到筛选的目的，分别对页面详细信息和页数统计文件进行移动分类
import shutil
import os
import re
from urllib import parse
import xml.etree.ElementTree as ET


def get_word(sword):
    string = parse.unquote(sword)
    string = parse.unquote(string)
    return string

# 用于移动页数统计文件
def move_file(xml_file):
    try:
        tree = ET.parse(xml_file)
    except:
        with open('error.txt','w') as file:
            file.write(xml_file)
        return None
    root = tree.getroot()
    num = root.find(".//num")
    if num is None:
        return None
    url = root.find('fullpath').text
    sfile_name = re.search(r"weibo/(\S*)&scope=ori", url).group(1)
    final_name = re.search(r"(\d*-\d*-\d*-\d*)", url).group(1)+".xml"
    #print(sfile_name)
    file_name = get_word(sfile_name)
    #print(file_name)
    try:
        shutil.move('./'+xml_file,'./'+file_name+'/'+final_name)
    except:
        print(xml_file)


# 用于移动页面统计文件
def move_page_file(xml_file):
    try:
        tree = ET.parse(xml_file)
    except:
        with open('error.txt','w') as file:
            file.write(xml_file)
        return None
    root = tree.getroot()
    contents = root.findall(".//content")
    sum_num = len(contents)
    url = root.find('fullpath').text
    sfile_name = re.search(r"weibo/(\S*)&scope=ori", url).group(1)
    final_name = re.search(r"(\d*-\d*-\d*-\d*)", url).group(1)+".xml"
    #print(sfile_name)
    file_name = get_word(sfile_name)
    # print(file_name)
    # print(xml_file)

    if file_name not in contents[0].text and word_dict.get(file_name) not in contents[0].text:
        return None
    try:
        shutil.move('./'+xml_file,'./'+file_name+'/'+final_name)
    except:
        print(xml_file)


os.chdir('D://rdata2//2//DataScraperWorks//悬浮_页数')
currentDirFiles = os.listdir("./")
#word_dict = {'人艰不拆':'人艱不拆','不明觉厉':'不明覺厲','扯淡':'扯淡','达人':'達人','淡定':'淡定','腹黑':'腹黑','纠结':'糾結','闷骚':'悶騷','山寨':'山寨','十动然拒':'十動然拒','完爆':'完爆'}
word_dict = {'接地气':'接地氣','吐槽':'吐槽','正能量':'正能量','自拍':'自拍'}
xmlFiles = [xmlFile for xmlFile in currentDirFiles if "xml" in xmlFile]
for xmlFile in xmlFiles:
    move_file(xmlFile)