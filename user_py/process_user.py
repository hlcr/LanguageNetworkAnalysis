import xml.etree.ElementTree as ET
import tool.util as util
import re
import pymysql
import traceback


def get_dict(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    r_dict = dict()

    # print(root.tag)
    ss = root.find('user/item/txt').text

    # 处理粉丝 微博 关注
    ii = root.find('user/item/inform').text
    if ii:
        ii = ii.replace("\t","")
        ll = ii.split("\n")
        while '' in ll:
            ll.remove('')
        for item in ll:
            r_dict[item[-2:]] = item[0:-2]
    else:
        r_dict["粉丝"] = 0
        r_dict["关注"] = 0
        r_dict["微博"] = 0

    # 添加用户id
    fullpath = root.find("fullpath").text
    r_dict["user_id"] = int(re.search(r"weibo\.com/(\d*)/info\?mod=pedit_more", fullpath).group(1))

    ss = ss.replace("\t","")
    ss = ss.replace("\n\n\n", "\n")
    ss = ss.replace("\n\n","\n")
    ss = ss.replace("\n\n","\n")
    ss = ss.replace("：\n","：")
    ll = ss.split("\n")
    for s in ll:
        if "：" in s:
            item = s.split("：")
            r_dict[item[0]] = item[1]
    return r_dict


def execute_user_sql(user_dict):
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='Ryan', db="wb_user",charset='UTF8')
    cur = conn.cursor()
    sql_str = "select * from user WHERE user_id = '{0}'".format(user_dict.get("user_id"))
    # print(sql_str)
    cur.execute(sql_str)
    try:
        if(cur.rowcount == 0):
            birthday = user_dict.get("生日","1000年01月01日").replace("年","-").replace("月","-").replace("日","")
            if "年" not in birthday:
                birthday = "1000-01-01"
            sql_str = "insert into user (user_id,nickname,place,birthday,rdate,follower,follow,weibo,sex) values ({0},'{1}','{2}','{3}','{4}',{5},{6},{7},'{8}')".format(user_dict.get("user_id"),user_dict.get("昵称"),user_dict.get("所在地"),birthday,user_dict.get("注册时间","1000-01-01"),user_dict.get("粉丝",0),user_dict.get("关注",0),user_dict.get("微博",0),user_dict.get("性别","无"))
    except(pymysql.err.IntegrityError):
        with open(r"D://semantic analysis//用户信息//sql_url_error.txt", "a",encoding='utf8') as file:
            file.write(sql_str + '\n')
            print('错误数据')
            print(sql_str)
            traceback.print_exc()
    cur.execute(sql_str)
    cur.close()                                    #关闭游标
    conn.commit()                                  #向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    conn.close()                                   #关闭到数据库的连接，释放数据库资源


def execute_url_sql():
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='Ryan', db="wb_user",charset='UTF8')
    cur = conn.cursor()
    sql_str = "select user_id from user"
    # print(sql_str)
    cur.execute(sql_str)
    with open(r'D:\semantic analysis\用户信息/user.txt', 'w', encoding='utf8') as w_file:
        for c in cur:
            w_file.write("http://weibo.com/" + str(c[0]) + "/info?mod=pedit_more" + '\n')

    cur.close()                                    #关闭游标
    conn.commit()                                  #向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
    conn.close()                                   #关闭到数据库的连接，释放数据库资源

# dd = "2010-01-18"
# dirr = r"D:\semantic analysis\用户信息\jj//" + dd + "//"
# f_list = util.get_file_list(dirr)
# r_dict = dict()
# for file in f_list:
#     rr = get_dict(dirr+file)
#     place = rr.get("所在地")
#     r_dict[place] = r_dict.get(place, 0) + 1
#
# util.save_dict_list(r_dict, r"D:\semantic analysis\用户信息\jj\dict//"+dd+".txt")



dd = r"D:\semantic analysis\用户信息\微博用户基本信息//"
ll = util.get_file_list(dd,".xml")
ii = 0
for file in ll:
    ii += 1
    while ii == 100:
        ii = 0
        print(file)
    rd_dict = get_dict(dd+file)
    execute_user_sql(rd_dict)

execute_url_sql()