import tool.util as util
# 计算所有文件里面所有词语出现的次数
key_list = util.get_key_list() + util.get_key_list2()
txt_dir = r"D:\semantic analysis\2016-10-09结果\词频1//"
r_dir = r"D:\semantic analysis\2016-10-09结果\总数1//"
for key in key_list:
    print(key)
    file_dir = txt_dir+key
    dict_list = []
    r_list = []
    file_list = util.get_file_list(file_dir, ".txt")
    for file_name in file_list:
        word_list = sorted(util.get_list_from_file(txt_dir+key+"//" + file_name))
        dict_list.append(util.txt2dict(word_list))

    r_dict = dict_list[0]
    for word_dict in dict_list:
        r_dict = util.union_dicts(r_dict, word_dict)

    # 对key进行排序
    kk = util.sort_by_value(r_dict)
    w_list = util.create_dict_list(kk, r_dict)

    # 创建目录
    util.save_file(r"D:\semantic analysis\2016-10-09结果\总数1//" + key + ".txt" , w_list, False)
