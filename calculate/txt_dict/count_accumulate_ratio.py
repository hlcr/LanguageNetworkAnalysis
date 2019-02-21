import tool.util as util

key_list = util.get_key_list()+util.get_key_list2()

fre_path = r"D:\semantic analysis\结果\去重频率//"
result_path = r"D:\semantic analysis\结果\累计位置前50//"

def get_acc_ratio(ratio_list):
    if len(ratio_list)-1 < 1:
        return 0
    s = 0
    for index, r in enumerate(ratio_list):
        s += r
        # if s > 0.6:
        #     return index/(len(ratio_list)-1)
        if index > 50 or index == len(ratio_list)-1:
            return s

for key in key_list:
    file_list = util.get_file_list(fre_path+key+"//",".txt")
    result_list = []
    for file in file_list:
        rl = util.get_list_from_dicttxt(fre_path+key+"//"+file)
        result_list.append(get_acc_ratio(rl))
    util.save_file(result_path+key+".txt",result_list)