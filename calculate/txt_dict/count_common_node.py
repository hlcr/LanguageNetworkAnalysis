import tool.util as util

key_list = ["山寨", "腹黑", "闷骚", "正能量", "扯淡", "达人", "纠结", "吐槽", "淡定", "自拍"]


for key in key_list:
    print(key)
    word_list = util.get_list_from_file(r"D:\semantic analysis\2016-10-12结果\2010年频数统计//"+key+".txt")
    s_dict = util.txt2dict(word_list)
    rank_key = util.sort_by_value(s_dict)
    high_index = -1
    low_index = -1
    high_value = int(s_dict[rank_key[0]] * 0.7)
    low_value = int(s_dict[rank_key[0]] * 0.01)
    # while high_index == -1:
    #     high_index = util.BinarySearch_Dict(rank_key, s_dict, high_value)
    #     high_value += 1
    high_index = 0
    low_value = 5

    while low_index == -1:
        low_index = util.BinarySearch_Dict(rank_key, s_dict, low_value)
        low_value -= 1

    # 生成统计的目标集合
    target_set = set()
    while low_index > high_index:
        target_set.add(rank_key[low_index])
        low_index -= 1
    node_sum = len(target_set)

    r_list = []
    r_list1 = []
    dict_list, key_dict_value = util.get_objdict_list(r"D:\semantic analysis\2016-10-09结果\词频月//"+key, ".txt")
    for dict_key in key_dict_value:
        word_dict = dict_list[dict_key]
        temp_set = set()
        for k, v in word_dict.items():
            temp_set.add(k)

        sum1 = len(temp_set & target_set)

        r_list.append(dict_key[0:-4] + "\t" + str(sum1))
        r_list1.append(dict_key[0:-4] + "\t" + str(sum1/node_sum))

    util.save_file(r"D:\semantic analysis\2016-10-12结果\2010年保留比例\新词\数量//"+key+".txt", r_list)
    util.save_file(r"D:\semantic analysis\2016-10-12结果\2010年保留比例\新词\比例//"+key+".txt", r_list1)


