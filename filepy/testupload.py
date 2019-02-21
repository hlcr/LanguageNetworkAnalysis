# 阿里云上传备份
import oss2
import time
import os
import shutil
from itertools import islice


Access_Key_ID = 'BjvM10cmtaCKpnuF'
Access_Key_Secret = 'tWChZrQKfjvTDD8FJQzm9m06mogE96'
endpoint = 'oss-cn-hangzhou.aliyuncs.com'
auth = oss2.Auth(Access_Key_ID, Access_Key_Secret)
service = oss2.Service(auth, endpoint, connect_timeout=30)
#print([b.name for b in oss2.BucketIterator(service)])
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'wbs')
print(bucket.bucket_name)
number = input('no:')
path = input('part:')
# C:\Users\Administrator\DataScraperWorks
#for b in islice(oss2.ObjectIterator(bucket), 10):
#    print(b.key)
#bucket.put_object_from_file('remote.txt', 'local.txt')
#bucket.get_object_to_file('remote.txt', 'local-backup.txt')
os.chdir(r'D:\recdate\hdusec-3\DataScraperWorks\search_part1')
if not os.path.exists('./ok'):
    os.mkdir('./ok')

ISOTIMEFORMAT='%Y-%m-%d %X'
file_list = []

while True:
    currentDirFiles = os.listdir("./")
    xmlFiles = [xmlFile for xmlFile in currentDirFiles if "xml" in xmlFile]

    # 清空上传成功的列表
    file_list.clear()
    print(time.strftime(ISOTIMEFORMAT, time.localtime()))
    # 迭代上传文件
    for xml_file in xmlFiles:
        result = bucket.put_object_from_file(number+'_'+xml_file, xml_file)
        if result.status == 200:
            try:
                # 移动上传成功的文件
                shutil.move('./'+xml_file,'./ok/'+xml_file)
                file_list.append([xml_file, result.request_id, result.headers['date']])
            except:
                print(xml_file)
        else:
            with open('error.txt','a') as err_file:
                err_file.write(xml_file+'\n')
    # 一轮上传结束后，输出信息并且记录下成功的文件信息
    print('finish!')
    with open('success.txt','a') as succ_file:
        for item in file_list:
            succ_file.write(item[0]+'\t'+item[1]+'\t'+item[2]+'\n')
    # 等待下一次上传
    time.sleep(1000)
