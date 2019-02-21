# 例：FTP编程
from ftplib import FTP
import os
import shutil
import time
import re


# 获取dir下所有xml文件的名字
def get_file_list(dir,type='.xml'):
    os.chdir(dir)
    currentDirFiles = os.listdir("./")
    return [xmlFile for xmlFile in currentDirFiles if type in xmlFile]


def get_time():
    import  time
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    return time.strftime(ISOTIMEFORMAT, time.localtime())

ftp = FTP()
timeout = 30
port = 21
dst_ip = "10.1.132.15"
name = "ryan"
password = "ryan"

# 本地文件存储的目录
local_dir = 'C://Users//Administrator//DataScraperWorks//search_part7//'

os.chdir(local_dir)
# 创建已经上传的目录
if not os.path.exists('./ok'):
    os.mkdir('./ok')

# 输入机子的号码
number = input("please input num:")
while number is None:
    number = input("please input num:")

while True:
    try:
        ftp.connect(dst_ip, port, timeout)  # 连接FTP服务器
        ftp.login(name, password)  # 登录
        file_list = ftp.nlst()  # 获得目录列表
        # 判断目录是否存在
        if number not in file_list:
            ftp.mkd(number)
        ftp.cwd('/'+str(number))  # 设置FTP路径

        xml_list = ftp.nlst()  # 获得目录已存在的列表
        local_list = get_file_list(local_dir, '.xml')
        with open(local_dir+'upload.txt', 'a') as r_file:
            for file in local_list:
                if file in xml_list:
                    # 创建已经上传失败的目录
                    if not os.path.exists('./fail'):
                        os.mkdir('./fail')
                    # 移动上传失败的文件
                    shutil.move('./' + file, './fail/' + file)
                else:
                    with open(local_dir + file, "rb") as f:
                        row1 = f.readline().decode("utf-8")
                        # 记录只有一页的页面
                        if r"<pageno>0</pageno>" in row1:
                            url = re.search(r"<fullpath><!\[CDATA\[(\S+)\]\]></fullpath>", row1).group(1)
                            print(url)
                            with open(local_dir + "one_page_record.txt", "a") as f1:
                                f1.write(url + "\n")
                        ftp.storbinary('STOR ' + file, f)
                    # 移动上传成功的文件
                    shutil.move('./' + file, './ok/' + file)
                    r_file.write(file+'\n')
        ftp.quit()  # 退出FTP服务器
        print(get_time())
        # 等待下一次上传
        time.sleep(600)
    except:
        print('=== STEP ERROR INFO START')
        import traceback
        traceback.print_exc()
        print('=== STEP ERROR INFO END')
        time.sleep(600)
