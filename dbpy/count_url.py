import pymysql
import tool.util as util

# 统计数据库里面的url的总条数
def get_sum_url():
    conn = pymysql.connect(host='10.1.132.105',  user='test', passwd='123456', db='cdata',charset='UTF8')
    cur = conn.cursor()
    sql_str = "select count(*) from url_record"
    cur.execute(sql_str)
    for ii in cur:
        cc = ii[0]
    cur.close()                                    #关闭游标
    conn.close()                                   #关闭到数据库的连接，释放数据库资源
    return cc

# 用于从数据库中提取失败的线索地址
def extract_address():
    # conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='123456', db='cdata',charset='UTF8')
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='Ryan', db='cdata2',charset='UTF8')
    cur = conn.cursor()

    sql_str = "SELECT * FROM url_record where eNum > 0 and cNum = 0;"
    cur.execute(sql_str)
    with open("raddress2.txt","w") as rfile:
        for ii in cur:
            rfile.write(ii[1]+'\n')
    cur.close()                                    #关闭游标
    conn.commit()                                  #向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    conn.close()                                   #关闭到数据库的连接，释放数据库资源


# 给定关键词，到数据库里面获得对应的条数
def get_count(keyword):
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='123456', db='cdata',charset='UTF8')
    cur = conn.cursor()
    sql_str = "select count(*) from "+util.getPY(keyword)
    cur.execute(sql_str)
    for ii in cur:
        cc = ii[0]
    cur.close()                                    #关闭游标
    conn.close()                                   #关闭到数据库的连接，释放数据库资源
    return cc