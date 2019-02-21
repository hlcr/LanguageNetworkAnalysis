import tool.util as util


def cal_union_set(keyword, pkl_dir):
    set_list = sorted(util.get_file_list(pkl_dir, "pkl"))
    r_list = []
    d_list = []
    i = 0
    r_set0 = set()
    while i < len(set_list):
        r_set0 = r_set0 | util.get_nw(pkl_dir + set_list[i])
        r_list.append(set_list[i][0:-4] + '\t' + str(len(r_set0)))
        d_list.append(len(r_set0))
        i += 1

    i = 0
    r_list2 = []
    d_list2 = []
    while i < len(r_list)-1:
        r_list2.append(set_list[i][0:-4] + '\t' + str(d_list[i+1]-d_list[i]))
        d_list2.append(d_list[i+1]-d_list[i])
        i += 1

    i = 15
    r_list3 = []
    while i < len(d_list2):
        r_list3.append(set_list[i][0:-4] + '\t' + str(d_list2[i]/d_list[i]))
        i += 1

    return r_list, r_list2,r_list3


key_list = util.get_key_list()
for key in key_list:
    print(key)
    r1, r2, r3 = cal_union_set(key, "D:\semantic analysis\分词集合//"+key+"//")
    # util.save_file(r"D:\semantic analysis\2016-10-03结果\增量//"+key+".txt", r2)
    # util.save_file(r"D:\semantic analysis\2016-10-03结果\总量//"+key+".txt", r1)
    util.save_file(r"D:\semantic analysis\2016-10-03结果\比例//"+key+".txt", r3)