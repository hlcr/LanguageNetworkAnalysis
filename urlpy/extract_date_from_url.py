import re
import tool.util as util
def extract_message(url):
    m1 = re.search(r"(\d+-\d+-\d+)",url)
    keyword = util.find_key_word(url)
    return keyword, m1.group(1)


def extract_keyword_date():
    keyword_set = set()
    with open(r"D:\semantic analysis\采集路线\2017-1-9\address2017-01-09.txt", "r") as f:
        url_list = f.readlines()
    for url in url_list:
        key, date = extract_message(url.strip())
        keyword_set.add(key)
        with open(key,"a") as file:
            file.write(date+"\n")

    for key in keyword_set:
        with open(key,"r") as file:
            key_set = set(file.readlines())
        with open(key,"w") as w_file:
            for k in key_set:
                w_file.write(k)


# extract_keyword_date()
import pymysql
import os

db_name = 'weibo'
dirr = r"D:\semantic analysis\新纯文本\1新词//"


def create_txt(keyword, date_str):
    os.chdir(dirr+keyword)
    # print(os.getcwd())
    py_keyword = util.getPY(keyword)
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='Ryan', db=db_name, charset='UTF8')
    cur = conn.cursor()

    sql_str = "select content from {0} where date = '{1}';".format(py_keyword,date_str )
    print(sql_str)
    cur.execute(sql_str)
    with open(date_str+'.txt', 'w', encoding='utf8') as w_file:
        for c in cur:
            w_file.write(c[0] + '\n'+ '\n')

    cur.close()                                    #关闭游标
    conn.close()                                   #关闭到数据库的连接，释放数据库资源

# key_list = ['完爆', '扯淡', '接地气', '正能量', '腹黑', '达人', '闷骚']
import time
key_list = ["喜欢"]
os.chdir(dirr)
for key_word in key_list:
    util.create_directory(key_word)
    # os.mkdir(key_word)

for key_word in key_list:
    with open(r"D:\semantic analysis\新纯文本\1新词/date/"+key_word,"r") as file:
        date_list = file.readlines()
    for date in date_list:
        create_txt(key_word,date.strip())


