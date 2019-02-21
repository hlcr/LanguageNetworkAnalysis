# 向数据库中插入数据
import pymysql
import os
import re
import xml.etree.ElementTree as ET
import tool.util as util
import traceback
import time

G_ID = 0
db_name = 'cdata2'


# 把信息插入到数据库中
def execute_data_sql(data_list, table_name):
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='123456', db=db_name,charset='UTF8')
    cur = conn.cursor()
    url_id = data_list[0]
    del(data_list[0])
    for item in data_list:
        try:
            try:
                sql_str = "insert into {0} (id,userid,content,passageUrl,terminal,forwardNum,commentNum,LikeNum,date,time,urlId) values ('{1}',{2},'{3}','{4}','{5}',{6},{7},{8},'{9}','{10}',{11});".format(table_name, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9],url_id)
                cur.execute(sql_str)
            except(pymysql.err.ProgrammingError):
                with open("D://semantic analysis//sql_error.txt", "a",encoding='utf8') as file:
                    traceback.print_exc()
                    file.write(sql_str + '\n')
                    print('正常数据')
                    print(sql_str)

        except(pymysql.err.IntegrityError):
            #sta=cur.execute("insert 语句")
            try:
                sql_str = "update {0} set repeatNum = repeatNum + 1 where id = '{1}';".format(table_name,item[0])
                cur.execute(sql_str)
            except(pymysql.err.ProgrammingError):
                with open("D://semantic analysis//sql_error1.txt", "a", encoding='utf8') as file:
                    file.write(sql_str + '\n')
                    print('错误数据')
                    print(sql_str)
                    traceback.print_exc()
            # print(sql_str)

    cur.close()                                    #关闭游标
    conn.commit()                                  #向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    conn.close()                                   #关闭到数据库的连接，释放数据库资源


# 插入url的记录
def execute_url_sql(url, e_num, c_num):
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='123456', db=db_name,charset='UTF8')
    cur = conn.cursor()
    sql_str = "select * from url_record WHERE url = '{0}'".format(url)
    # print(sql_str)
    cur.execute(sql_str)
    # 使用了全局变量
    global G_ID
    uid = G_ID
    try:
        if(cur.rowcount > 0):
            G_ID -= 1
            for ii in cur:
                uid = ii[0]
            sql_str = "update url_record set cNum = cNum+{0}, eNum = eNum+{1}, repeatNum = repeatNum+1 where urlid = '{2}'".format(c_num,e_num,uid)
        else:
            sql_str = "insert into url_record (urlid,url,cNum,eNum) values ({0},'{1}',{2},{3})".format(uid,url,c_num,e_num)
            # print(sql_str)
    except(pymysql.err.IntegrityError):
        with open("D://semantic analysis//sql_url_error.txt", "a",encoding='utf8') as file:
            file.write(sql_str + '\n')
            print('错误数据')
            print(sql_str)
            traceback.print_exc()
    cur.execute(sql_str)
    cur.close()                                    #关闭游标
    conn.commit()                                  #向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    conn.close()                                   #关闭到数据库的连接，释放数据库资源
    return uid


# 处理文件返回有效数据list，错误数据list，处理的url0
def process_file(file):
    global G_ID
    G_ID += 1
    tree = ET.parse(file)
    root = tree.getroot()
    url = root.find('fullpath').text
    # 获取数据列表
    data_list = util.get_item_list(root)

    # 获取关键词
    keyword = util.find_key_word(url)
    c_list = []
    e_list = []
    # url的id
    for item in data_list:
        if(util.isValid(keyword,item[2])):
            c_list.append(item)
        else:
            e_list.append(item)

    # 插入url
    uuid = execute_url_sql(url, len(e_list), len(c_list))

    # 插入错误数据
    if e_list != []:
        e_list.insert(0, uuid)
        execute_data_sql(e_list, 'err_data')

    # 插入正常数据
    if len(c_list) !=  []:
        c_list.insert(0, uuid)
        execute_data_sql(c_list,util.getPY(keyword))
    return c_list, e_list, url


# os.chdir('D://semantic analysis//2次采集//页面统计')
# currentDirFiles = os.listdir("./")
# xmlFiles = [xmlFile for xmlFile in currentDirFiles if "xml" in xmlFile]
# for xmlFile in xmlFiles:
#     move_page_file(xmlFile)
def get_max():
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='123456', db=db_name,charset='UTF8')
    cur = conn.cursor()
    sql_str = "select MAX(urlid) from url_record"
    cur.execute(sql_str)
    for ii in cur:
        cc = ii[0]
    cur.close()                                    #关闭游标
    conn.close()                                   #关闭到数据库的连接，释放数据库资源
    if cc == None:
        cc = 0
    return cc



G_ID = get_max()
print(G_ID)
# with open('path.txt','r',encoding='utf8') as file:
#     dir_list = file.readlines()

dirr = 'D://back//'
os.chdir(dirr)
dir_list = os.listdir("./")
for dd in dir_list:
    print(dd)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    xml_files = util.get_file_list(dirr+dd)
    for item in xml_files:
        try:
            process_file(item)
        except(ET.ParseError):
            with open(dirr+'err_file_record.txt', 'a') as record_file1:
                print('err_file'+item)
                record_file1.write(item+'\n')
        with open('record.txt', 'a') as record_file:
            record_file.write(item+'\n')


