# 根据初步采集结果来生成最后的采集结果
# 具体原则为 如果大于20页就生成每个小时的采集结果，否则返回原来的结果
import xml.etree.ElementTree as ET
import re
import os
import random
from urllib import parse



def create_url_word(sword):
    string = parse.quote(sword)
    strArray = string.split('%')
    rword = ''
    for i in range(1,len(strArray)):
        rword += ('%25'+strArray[i])
    return rword


def create_address(xmlFile,sword):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    url = root.find('fullpath').text
    # 查找页数
    num = root.find(".//num")
    # 对标志信息进行查找
    firstDate = int(re.search(r"custom:\d*-\d*-\d*-(\d*)", url).group(1))
    lastDate = int(re.search(r"\d*-\d*-\d*-(\d*)&", url).group(1))
    Date = re.search(r"(\d*-\d*-\d*)", url).group(1)
    if num != None:
        maxpage = re.search(r"(\d+)", num.text[-3:]).group(1)
    if int(maxpage) <= 20:
        return [url]
    else:
        alist = []
        i = firstDate
        while i <= lastDate:
            curl = 'http://s.weibo.com/weibo/'+sword+'&scope=ori&suball=1&timescope=custom:'+Date+'-'+str(i)+':'+Date+'-'+str(i)+'&Refer=g'
            alist.append(curl)
            i += 1
        return alist


def create(file_dir,sword):
    if file_dir is not None:
        os.chdir(file_dir)
    addresslist = []
    currentFiles = os.listdir('./')
    xmlFiles = [xmlfile for xmlfile in currentFiles if '.xml' in xmlfile]
    for xmlFile in xmlFiles:
        alist = create_address(xmlFile,sword)
        for item in alist:
            addresslist.append(item)

    with open('address.txt','w') as resultfile:
            for item in addresslist:
                    resultfile.write(item+'\n')

#word_dict = {'人艰不拆':'人艱不拆','不明觉厉':'不明覺厲','扯淡':'扯淡','达人':'達人','淡定':'淡定','腹黑':'腹黑','纠结':'糾結','闷骚':'悶騷','山寨':'山寨','十动然拒':'十動然拒','完爆':'完爆'}
word_dict = {'接地气':'接地氣','吐槽':'吐槽','正能量':'正能量','自拍':'自拍'}
#os.chdir('D://semantic analysis//2次采集//页数统计')
for (k, v) in word_dict.items():
    print(k)
    create('D://rdata2//2//DataScraperWorks//悬浮_页数//'+k, create_url_word(k))
