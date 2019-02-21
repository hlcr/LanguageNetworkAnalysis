import tool.util as util
import os
# 统计所有关键词出现的文件数


def count_word(word_set, word_dict):
    for word in word_set:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict[word] + 1


def count_word_from_dict(new_dict, word_dict):
    for word, v in new_dict.items():
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict[word] + 1


dir = r"D:\semantic analysis\2016-10-09结果\词频月//"
key_list = util.get_key_list()

for key in key_list:
    os.chdir(dir+key)
    print(key)
    file_list = util.get_obj_list(dir+key,".txt")
    r_word_dict = dict()
    for file in file_list:
        count_word_from_dict(file, r_word_dict)
    util.save_dict_list(r_word_dict,r"D:\semantic analysis\2016-10-12结果\总频数月//"+key+".txt")
