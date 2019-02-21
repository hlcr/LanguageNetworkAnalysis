import tool.util as util

def get_num_sentence(file_path):
    return len(set(util.get_list_from_file(file_path)))

key_list = util.get_key_list2()


root = r"D:\semantic analysis\新纯文本\1常用词/"
for key in key_list:
    print(key)
    file_list = util.get_file_list(root+key,".txt")
    r_list = []
    for file in file_list:
        ss = get_num_sentence(root+key+"//"+file)
        r_list.append(file[0:-4] + "\t" + str(ss))
    util.save_file(r"D:\semantic analysis\新结果//去重句子数//常用词//"+key+".txt",r_list)