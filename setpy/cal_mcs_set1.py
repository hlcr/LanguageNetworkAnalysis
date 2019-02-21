import os
import tool.util as util


def cal_mcs(pkl_dir):
    os.chdir(pkl_dir)
    pkl_list = util.get_file_list(pkl_dir, '.pkl')
    # 从小到大排序
    pkl_list = sorted(pkl_list)

    r_set = set()
    r_set1 = set()
    i = 0
    while i < 40:
        set1 = util.get_nw(pkl_list[i])
        set2 = util.get_nw(pkl_list[len(pkl_list)-1-i])
        r_set = set1 | r_set
        r_set1 = set2 | r_set1
        i += 1

    print(len(r_set))
    print(len(r_set1))

    r_set2 = r_set & r_set1
    print(len(r_set2))
    print(len(r_set2)/len(r_set))


key_list = util.get_key_list()
for key in key_list:
    print()
    print(key)
    cal_mcs(r"D:\semantic analysis\分词集合//"+key + "//")

print("-----------------------------------------------------------")
key_list = util.get_key_list()
for key in key_list:
    print()
    print(key)
    cal_mcs(r"D:\semantic analysis\分词集合1//"+key + "//")