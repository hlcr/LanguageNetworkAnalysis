import tool.util as util


# d 是dict
# 返回按照value降序排序后的 key 列表
def sort_by_value(d):
    items=d.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort(reverse = True)
    return [ backitems[i][1] for i in range(0,len(backitems))]


# sort_key_list: 排序后的key
# word_dict: 待保存的字典
def create_dict_list(sort_key_list, word_dict):
    word_list = []
    for key in sort_key_list:
        if len(key) > 1:
            vv = word_dict[key]
            word_list.append(key+"\t"+str(vv))
    return word_list


# 统计每天分句的词频
def count_word(sentences, keyword):
    r_dict = dict()
    for sentence in sentences:
        # 过滤并把一个句子切成分句
        spl = util.get_word_list(sentence, keyword)
        for sp in spl:
            for word in sp:
                if word in r_dict:
                    r_dict[word] = r_dict.get(word) + 1
                else:
                    r_dict[word] = 1
    return r_dict



# 结巴分词词典的目录
# jieba.set_dictionary("D:\semantic analysis\分词\词库\导出结果\dict1.txt")
# jieba.initialize()

import pynlpir
from ctypes import c_char_p
key_word = ["喜欢"]
pynlpir.open()
for key in key_word:
    print(key)
    pynlpir.nlpir.AddUserWord(c_char_p(key.encode()))


result_dir = r"D:\semantic analysis\新结果\去重去虚词去单字词频数//"
fold_list_dir = r"D:\semantic analysis\新纯文本\1常用词分句//"
for key in key_word:
    print(key)
    file_list = sorted(util.get_file_list(fold_list_dir+key, ".txt"))
    # 循环文件
    for txt_file in file_list:
        print(txt_file)
        # 过滤重复
        s_list = set(util.get_list_from_file(fold_list_dir+key+"//"+txt_file))
        # 获取分词dict
        rr = count_word(s_list, key)
        # if "无力" in rr:
        #     print(rr["无力"]/rr["吐槽"])

        # 对key进行排序
        kk = sort_by_value(rr)
        w_list = create_dict_list(kk, rr)

        # 创建目录
        util.create_directory(result_dir+key)
        util.save_file(result_dir+key+"//"+txt_file, w_list, False)

# 关闭分词工具
pynlpir.close()
