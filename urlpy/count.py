# 用于页数的累加统计
import xml.etree.ElementTree as ET
import re, os


def count(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    url = root.find('fullpath').text
    num = root.find(".//num")
    if num != None:
        date = re.search(r"(\d*-\d*-\d*)", url).group(1)
        maxpage = re.search(r"(\d+)", num.text[-3:]).group(1)
        return date,int(maxpage)
    return None,None

def file_count(file_dir):
    if file_dir is not None:
        os.chdir(file_dir)
    currentFiles = os.listdir('./')
    xmlFiles = [xmlfile for xmlfile in currentFiles if '.xml' in xmlfile]
    numdict = dict()
    for xmlFile in xmlFiles:
        date,maxpage = count(xmlFile)
        if date != None:
            if maxpage > 0:
                numdict[date] = maxpage + numdict.get(date,0)
    with open('result.txt','w') as resultfile:
            for (k,v) in numdict.items():
                    resultfile.write(str(k)+'\t'+str(v)+'\n')

word_dict = {'人艰不拆':'人艱不拆','不明觉厉':'不明覺厲','扯淡':'扯淡','达人':'達人','淡定':'淡定','腹黑':'腹黑','纠结':'糾結','闷骚':'悶騷','山寨':'山寨','十动然拒':'十動然拒','完爆':'完爆'}
#os.chdir('D://semantic analysis//2次采集//页数统计')
for (k,v) in word_dict.items():
    print(k)
    file_count('D://semantic analysis//2次采集//页数统计//'+k)
