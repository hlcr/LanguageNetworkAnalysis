import tool.util as util
import os

# 获取一个关键词的所有条数
def get_len(file):
    return len(util.get_list_from_file(file))

key_list =  ['努力', '感觉', '简单', '无聊', '希望', '美好', '气质', '害怕', '喜欢']

for key in key_list:
    file_list = util.get_file_list("D:\semantic analysis\纯文本\常用词//"+key+"//", ".txt")[-68:-1]
    os.chdir("D:\semantic analysis\纯文本\常用词//"+key+"//")
    s_sum = 0
    for file in file_list:
        s_sum += len(util.get_list_from_file(file))
    print(key + "\t" + str(s_sum))

