import re
import tool.util as util


key_list = util.get_key_list()

dict_dir = r"D:\semantic analysis\2016-10-09结果\词频1//"
for key in key_list:
    print(key)
    set_dict,file_name = util.get_objdict_list(dict_dir+key, ".txt")
    date_list = util.get_file_list(dict_dir+key, ".txt")
    pattern = re.compile(r"(\d*-\d*)-\d*")
    month_array = pattern.findall(" ".join(date_list))
    month_array = ["2010"]

    util.create_directory(r"D:\semantic analysis\2016-10-12结果\2010年频数统计//" + key)

    # 循环查找月份
    for month in month_array:
        pattern = re.compile(r"(" + month + "-\d*-\d*)")
        date_array = pattern.findall(" ".join(date_list))
        print(date_array)
        # 循环合并月份频数字典
        r_dict = dict()
        for file_date in date_array:
            r_dict = util.union_dicts(set_dict[file_date+".txt"], r_dict)
        util.save_dict_list(r_dict, r"D:\semantic analysis\2016-10-12结果\2010年频数统计//"+key+".txt")



