import tool.util as util

# 寻找是否存在某特定的词语
def function_1(s_list, word):
    for aa in s_list:
        if word in aa:
            return True
    return False


key_list = ["害怕"]
dir = "D:\semantic analysis\纯文本\常用词//"

for key in key_list:
    file_list = util.get_file_list(dir+key, ".txt")
    for file in file_list:
        s_list = util.get_list_from_file(dir+key+"//"+file)
        if not function_1(s_list,"地铁"):
            print(file)