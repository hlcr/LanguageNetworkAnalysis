# 数据库提取数据，每个关键词提取到每个txt文件中
import pymysql
import util
import os

db_name = 'cdata2'
dirr = r"D:\semantic analysis\常用词\\"


def create_txt(keyword):
    os.chdir(dirr+keyword)
    # print(os.getcwd())
    py_keyword = util.getPY(keyword)
    conn = pymysql.connect(host='127.0.0.1',  user='root', passwd='123456', db=db_name, charset='UTF8')
    cur = conn.cursor()
    sql_str = "select distinct date from {0};".format(py_keyword)
    print(sql_str)
    cur.execute(sql_str)
    t_list = list(cur)
    for dd in t_list:
        date_str = dd[0].isoformat()
        sql_str = "select content from {0} where date = '{1}';".format(py_keyword,date_str )
        print(sql_str)
        cur.execute(sql_str)
        with open(date_str+'.txt', 'w', encoding='utf8') as w_file:
            for c in cur:
                w_file.write(c[0] + '\n'+ '\n')

    cur.close()                                    #关闭游标
    conn.close()                                   #关闭到数据库的连接，释放数据库资源

# key_list = ['吐槽','正能量','接地气','自拍','达人','淡定','腹黑','纠结','闷骚','山寨','十动然拒','完爆','接地气','正能量','自拍','吐槽']

# '不约而同', '喜闻乐见', '努力', '感觉', '简单', '无聊', '希望', '美好','气质','害怕','喜欢'
key_list = ['不约而同', '喜闻乐见', '努力', '感觉', '简单', '无聊', '希望', '美好','气质','害怕','喜欢']

os.chdir(dirr)
for key_word in key_list:
    util.create_directory(key_word)
    # os.mkdir(key_word)

for key_word in key_list:
    create_txt(key_word)

