from tool.util import *

txt_path = "D:\semantic analysis\新结果\去虚词去单字\k-core保留//"
key_word_list = get_key_list() + get_key_list2()
result_list = []
for key in key_word_list:
    float_list = get_list_from_dicttxt(txt_path+key+".txt")
    result_list.append(key + '\t' + str(average(float_list)) + '\t' + str(variance(float_list)))

for item in result_list:
    print(item)
