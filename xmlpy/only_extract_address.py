# 提取所有xml中的地址
import xml.etree.ElementTree as ET
import os

os.chdir('D://bb//ok//')
currentDirFiles = os.listdir("./")
xmlFiles = [xmlFile for xmlFile in currentDirFiles if ".xml" in xmlFile]
addressList = []
for xmlFile in xmlFiles:
    try:
        tree = ET.parse(xmlFile)
    except:
        print(xmlFile)
    root = tree.getroot()
    url = root.find('fullpath').text
    addressList.append(url)

with open('address.txt','w') as file:
    for item in addressList:
        file.write(item+'\n')