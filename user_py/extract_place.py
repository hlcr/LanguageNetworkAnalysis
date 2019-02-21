import pymysql
import tool.util as util


def get_place(user_id):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Ryan', db="wb_user", charset='UTF8')
    cur = conn.cursor()
    sql_str = "select place from user WHERE user_id = '{0}'".format(user_id)
    # print(sql_str)
    cur.execute(sql_str)
    place = None
    if cur.rowcount != 0:
        for c in cur:
            place = c[0]

    cur.execute(sql_str)
    cur.close()  # 关闭游标
    conn.commit()  # 向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    conn.close()  # 关闭到数据库的连接，释放数据库资源
    return place


def extract_user_id(py_keyword, date_str):
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='Ryan', db='cdata',charset='UTF8')
    cur = conn.cursor()
    sql_str = "select userid from {0} where date = '{1}';".format(py_keyword, date_str)
    print(sql_str)
    r_list = []
    cur.execute(sql_str)
    with open('userUrl.txt', 'a', encoding='utf8') as w_file:
        for c in cur:
            r_list.append(c[0])

    cur.close()                                    #关闭游标
    conn.commit()                                  #向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    conn.close()                                   #关闭到数据库的连接，释放数据库资源
    return r_list


date_list_list = [["2010-01-03",
"2010-02-09",
"2010-07-21",
"2010-11-14",
"2011-04-26"],["2010-01-03",
"2010-04-03",
"2010-07-03",
"2010-10-14"],
["2010-01-08",
"2010-02-01",
"2010-03-13",
"2010-04-22",
"2010-06-12",
"2010-07-27",
"2010-09-30",
"2010-11-12",
"2011-01-05",
"2011-03-03",
"2011-04-24",
"2011-06-24",
"2011-08-19"],
["2010-01-17",
"2010-02-20",
"2010-03-18",
"2010-04-29",
"2010-05-28",
"2010-07-01",
"2010-08-10",
"2010-12-24",
"2011-03-05",
"2011-04-14",
"2011-07-04",
"2011-10-11",
"2011-11-21"],
["2010-03-19",
"2010-05-03",
"2010-06-12",
"2010-09-17",
"2010-11-29",
"2011-01-23",
"2011-04-01",
"2011-08-20",
"2011-12-22"],
["2010-05-15",
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
             ]
py_list = ["zp","dd","sz","dr","ms","fh"]

date_list_list = [["2010-06-01",
"2011-01-21",
"2011-07-09",
"2011-11-21"]]
py_list = ["tc"]
root_path = r"D:\semantic analysis\用户信息\dict//"
i = 0
while i < len(py_list):
    py = py_list[i]
    date_list = date_list_list[i]
    i += 1
    for dd in date_list:
        user_id_list = extract_user_id(py,dd)
        place_list = []
        place_dict = dict()
        if user_id_list:
            for user_id in user_id_list:
                place = get_place(user_id)
                if place:
                    place_list.append(place)
            place_dict = dict((a, place_list.count(a)) for a in place_list)
            util.create_directory(root_path+py)
            util.save_dict_list(place_dict, root_path+py+"//"+dd+".txt")
