import pymysql
import os
import re
import tool.util as util

def extract_url(py_keyword,date_str):
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='Ryan', db='cdata',charset='UTF8')
    os.chdir(r"D:\semantic analysis\用户信息//")
    # cur = conn.cursor()
    # sql_str = "SELECT * FROM url_record where eNum > 0 and cNum = 0;"
    # cur.execute(sql_str)

    cur = conn.cursor()
    # sql_str = "select distinct date from {0};".format(py_keyword)
    # print(sql_str)
    # cur.execute(sql_str)
    # t_list = sorted(list(cur))
    # t_list = sorted(list(cur))
    # print(t_list)

    # for dd in t_list[33]:
    # date_str = dd[0].isoformat()
    sql_str = "select userid from {0} where date = '{1}';".format(py_keyword, date_str)
    print(sql_str)
    cur.execute(sql_str)
    with open('userUrl.txt', 'a', encoding='utf8') as w_file:
        for c in cur:
            w_file.write("http://weibo.com/" + str(c[0]) + "/info?mod=pedit_more" + '\n')


    # with open("raddress2.txt","w") as rfile:
    #     for ii in cur:
    #         rfile.write(ii[1]+'\n')
    cur.close()                                    #关闭游标
    conn.commit()                                  #向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    conn.close()                                   #关闭到数据库的连接，释放数据库资源


dd = ["2010-05-15",
"2010-08-02",
"2010-09-26",
"2010-11-03",
"2011-01-11",
"2011-03-20",
"2011-06-01",
"2011-10-16",
"2012-02-16",
"2012-07-09",
"2012-11-19"]

for d in dd:
    extract_url("fh",d)



ll = util.get_list_from_file(r"D:\semantic analysis\用户信息//userUrl.txt")
lll = util.get_list_from_file(r"D:\semantic analysis\用户信息//user.txt")
print(len(ll))
ss = set(ll)
ss1 = set(lll)
print(len(ss))
ss = ss - ss1
print(len(ss))
ll = list(ss)
util.save_file(r"D:\semantic analysis\用户信息//userUrl1.txt",ll)
