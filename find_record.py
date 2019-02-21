# 检查是否有 record.txt 有的话,就删掉
import shutil
import os

dirr = 'D://back//'
os.chdir(dirr)
d_list = os.listdir("./")



# with open('path.txt','r') as f:
# d_list = f.readlines()
for dir in d_list:
    dir = dir.strip('\n')
    if os.path.exists(dirr+dir + '\\' + 'record.txt'):
        print(dir)
        shutil.rmtree(dir)




