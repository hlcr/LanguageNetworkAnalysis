# 用于字典的去重
import os
os.chdir(r'D:\semantic analysis\分词\词库\ok')

current_files = os.listdir("./")
txt_list = [txt_file for txt_file in current_files if '.txt' in txt_file]

# 最终的字典数组
dict_list = []
for txt in txt_list:
    # 遍历读文件
    with open(txt, 'r', encoding='utf-8') as txt_file:
        txt_list = txt_file.readlines()
        # 遍历每个词
        for word in txt_list:
            word = word.strip('\n')
            # 过滤掉 大于 4 个字的词语
            if len(word) < 5:
                # 判断是已经存在
                if word not in dict_list:
                    dict_list.append(word)

with open('result_dict.txt','w', encoding='utf-8') as r_file:
    for word in dict_list:
        r_file.write(word+'\n')
