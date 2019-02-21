import re
import tool.util as util


key_list = util.get_key_list2()

dict_dir = r"D:\semantic analysis\2016-10-09结果\词频1//"
r_dict = dict()
for key in key_list:
    print(key)
    set_dict = util.get_obj_list(dict_dir+key, ".txt")
    for file_date in set_dict:
        r_dict = util.union_dicts(file_date, r_dict)

util.save_dict_list(r_dict, r"D:\百度指数截屏//常用词总频率统计"+".txt")



