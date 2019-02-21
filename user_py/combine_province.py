import tool.util as util
root_path = r"D:\semantic analysis\用户信息\dict//"
save_root_path = r"D:\semantic analysis\用户信息\s_dict//"


def combine(src_path, save_path):
    file_list_dict, file_name_list = util.get_objdict_list(src_path, ".txt")
    for file_name, file_dict in file_list_dict.items():
        r_dict = dict()
        for place, num in file_dict.items():
            p_place = place.split(" ")[0]
            r_dict[p_place] = r_dict.get(p_place, 0) + num
        util.save_dict_list(r_dict,save_path+file_name)

py_list = ["tc","zp","dd","sz","dr","ms","fh","znl"]
for py in py_list:
    util.create_directory(save_root_path+py+"//")
    combine(root_path+py+"//",save_root_path+py+"//")