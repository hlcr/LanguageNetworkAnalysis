import tool.util as util
import os


def cal_disappear(ori_set, new_set):
    return ori_set - new_set


# date_list: 分段时间
# pkl_dir: pkl的路径
def cal_index(date_list, pkl_dir):
    r_list = []
    f_list = util.get_file_list(pkl_dir, '.pkl')
    os.chdir(pkl_dir)
    # 升序排序
    set_list = sorted(f_list)

    date2 = set_list[0][0:-4]
    i = 0
    for date in date_list:
        date1 = date
        # 查找出分割点所在的序号
        while i < len(set_list) and util.compare_date(date1, date2) > 0.0:
            date2 = set_list[i][0:-4]
            i += 1
        r_list.append(i)
    r_list.append(len(f_list))
    return r_list

# date_list: 分段时间
# pkl_dir: pkl的路径
# 除了第一个是按照时间来，其他平分
def cal_index2(date, pkl_dir):
    r_list = []
    f_list = util.get_file_list(pkl_dir, '.pkl')
    os.chdir(pkl_dir)
    # 升序排序
    set_list = sorted(f_list)

    date2 = set_list[0][0:-4]
    i = 0
    date1 = date
    # 查找出分割点所在的序号
    while i < len(set_list) and util.compare_date(date1, date2) > 0.0:
        date2 = set_list[i][0:-4]
        i += 1
    r_list.append(i)

    j = 0
    part = 3
    part_num = (len(f_list) - i) // part
    while j < part-1:
        j += 1
        r_list.append(i + j * part_num)

    r_list.append(len(f_list))
    return r_list


def cal_difference(index_list, set_list):
    # 存储结果的集合
    r_list = []
    # 升序排列
    set_list = sorted(set_list)
    k = 0
    for index in index_list:
        s1 = set()
        # 进行合并集合操作
        while k < index:
            s1 = set_list[k] | s1
            k += 1
        # 把中间集合添加到结果中
        r_list.append(s1)

    # 最后目标集合
    rd_list = []
    j = 0
    while j < len(r_list) - 1:
        rd_list.append(cal_disappear(r_list[j],r_list[j+1]))
        j += 1

    # 差集, 原来集合
    return rd_list, r_list


# dd = "2010-02-09"
# rr = cal_index2(dd,r"D:\semantic analysis\分词集合\自拍//")
# print(rr)

# date_list = ["2012-08-05","2011-04-05","2011-03-28","2011-10-20","2012-12-30","2011-07-30","2011-06-09","2012-02-05","2012-12-16","2011-08-01","2011-05-19","2013-09-01","2012-08-01","2013-12-01"]
# key_list = ["吐槽","纠结","淡定","自拍","正能量","山寨","达人","腹黑","接地气","扯淡","闷骚","不明觉厉","完爆","人艰不拆"]

date_list = ["2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31"]
key_list = util.get_key_list2()


k = 0
for key in key_list:
    print(key)
    dir = "D:\semantic analysis\常用词的分词集合//"
    # index_list = cal_index2(date_list[k], dir+key)
    index_list = [100,125,150]
    print(index_list)
    k += 1
    file_list = util.get_file_list(dir+key, ".pkl")
    set_list = []
    # 获取目录下所有set集合
    os.chdir(dir+key)
    for file in file_list:
        set_list.append(util.get_nw(file))
        # print(len(set_list))
    rd_list, r_list = cal_difference(index_list, set_list)
    r_dir = r"D:\semantic analysis\2016-10-09结果\中间结果//"
    util.create_directory(r_dir+key)
    i = 0
    while i < len(rd_list):
        print(len(rd_list[i]))
        print(len(r_list[i]))
        print(len(rd_list[i])/len(r_list[i]))
        # util.save_nw(r_set, r_dir+key+"//"+str(index_list[i]).zfill(3)+".pkl")
        i += 1





