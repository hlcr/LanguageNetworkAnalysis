import tool.util as util


# 求出dict2 & dict1 的value 在 dict2  / dict2 数值
def cal_mcs_ratio(dict1, dict2, keyword):
    m_dict = dict()
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    inter_list = util.inter_dicts(dict1, dict2)

    # inter_list.remove(keyword)
    # 求出公共集合在 dict2 的总数
    for word in inter_list:
        num2 = dict2[word]
        sum2 += int(num2)
        m_dict[word] = num2

    # dict1.pop(keyword)
    # 求出dict2的总节点数
    for k, v in dict2.items():
        sum1 += int(v)

    # 求出公共集合在 dict2 的总数
    for word in inter_list:
        num3 = dict1[word]
        sum3 += int(num3)
        m_dict[word] = num3

    # dict1.pop(keyword)
    # 求出dict2的总节点数
    for k, v in dict1.items():
        sum4 += int(v)


    return sum2


def test():
    dict1 = dict()
    dict2 = dict()

    dict1["我"] = 2
    dict2["我"] = 1

    dict1["你"] = 2
    dict2["他"] = 1

    dict1["不"] = 2
    dict2["怎"] = 1

    dict1["哈"] = 2
    dict2["哈"] = 1

    dict3 = util.union_dicts(dict1, dict2)
    print(dict3)
    sl = util.inter_dicts(dict1, dict2)
    print(sl)
    print(cal_mcs_ratio(dict1,dict2,))
    w_list = util.get_list_from_file(r"D:\semantic analysis\2016-10-09结果\词频\希望//2011-09-30.txt")
    dd = util.txt2dict(w_list)



key_list = util.get_key_list2()+util.get_key_list()
txt_dir = r"D:\semantic analysis\2016-10-09结果\词频1//"
for key in key_list:
    print(key)
    file_dir = txt_dir+key
    dict_list = []
    r_list = []
    file_list = util.get_file_list(file_dir,".txt")
    for file_name in file_list:
        word_list = sorted(util.get_list_from_file(txt_dir+key+"//" + file_name))
        dict_list.append(util.txt2dict(word_list))

    # 循环求比值
    i = 1
    dict1 = dict_list[0]
    while i < len(dict_list):
        dict2 = dict_list[i]
        r_list.append(file_list[i-1][0:-4] + "\t" + str(cal_mcs_ratio(dict1, dict2, key)))
        dict1 = dict2.copy()
        i += 1

    util.save_file(r"D:\semantic analysis\2016-10-12结果\自身比例节点数//"+key+".txt", r_list, False)
