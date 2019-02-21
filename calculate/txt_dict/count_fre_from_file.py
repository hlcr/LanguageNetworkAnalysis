import tool.util as util

# 从每个dict——txt文件里面统计词频率
dict_path=r"D:\semantic analysis\结果\去重频数//"
result_path=r"D:\semantic analysis\结果\去重频率//"

keyword_list = util.get_key_list2() + util.get_key_list()

for key in keyword_list:
    print(key)
    r_dict, file_name_list = util.get_objdict_list(dict_path+key,".txt")
    for (k,word_dict) in r_dict.items():
        sum = 0
        r_f_dict = {}
        if key in word_dict:
            word_dict.pop(key)
        for word, value in word_dict.items():
            sum += int(value)
        for word, value in word_dict.items():
            ratio = value/sum
            r_f_dict[word] = ratio
        util.create_directory(result_path+key+"//")
        util.save_dict_list(r_f_dict,result_path+key+"//"+k)