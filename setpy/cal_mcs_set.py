import os
import tool.util as util


def cal_mcs(div, num, pkl_dir):
    os.chdir(pkl_dir)
    pkl_list = util.get_file_list(pkl_dir, '.pkl')
    # 从小到大排序
    pkl_list = sorted(pkl_list)
    # part_num = len(pkl_list) // div
    part_num = 200
    print("part_nume")
    print(part_num)
    if part_num < num:
        print("参数有误")
        return
    i = 0
    set_list = []
    # 块内的循环
    while i < div:
        # 进行合并操作
        j = 0
        r_set = set()
        while j < num:
            pkl_num = part_num * i + j
            set1 = util.get_nw(pkl_list[pkl_num])
            r_set = set1 | r_set
            j += 1
        # 把合并的结果加入列表中
        set_list.append(r_set)
        print(len(r_set))
        i += 1

    # 进行比值运算
    # i = 0
    # while i < len(set_list) - 1:
    #     mcs_set = set_list[i] & set_list[i+1]
    #     print(len(mcs_set)/len(set_list[i]))
    #     i += 1


key_list = util.get_key_list()
for key in key_list:
    print()
    print(key)
    cal_mcs(2, 5, r"D:\semantic analysis\分词集合1//"+key + "//")
