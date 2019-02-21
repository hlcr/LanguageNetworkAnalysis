from ctypes import c_char_p

import tool.util as util
import jieba


def zky(s):
    import pynlpir
    pynlpir.open()
    keyword = "美好"
    pynlpir.nlpir.AddUserWord(c_char_p(keyword.encode()))
    # w_list = list(pynlpir.segment(s,pos_tagging=False))
    w_list = list(pynlpir.segment(s,pos_english=False))
    exclude_set = ("副词", "介词", "连词", "助词", "叹词", "语气词", "拟声词")

    quote_list = []
    kpl = []
    index = 0
    print(w_list)

    while index < len(w_list):
        item = w_list[index]
        if item[1] in exclude_set:
            w_list.remove(item)
            index -= 1
        elif item[1] == '标点符号':
            quote_list.append(index)
        elif item[0] == keyword:
            kpl.append(index)
        index += 1



    print(quote_list)
    print(kpl)

    word_list = []
    print(w_list)
    for kp in kpl:
        for i,p in enumerate(quote_list):
            if kp <= p:
                word_list.append(w_list[quote_list[i-1]+1:quote_list[i]])
                break

    result_word_list =[]
    for sentence in word_list:
        temp_list = []
        for word in sentence:
            temp_list.append(word[0])
        result_word_list.append(temp_list)

    pynlpir.close()
    return result_word_list

# 获取分词的list
def get_word_list(sentence):
    seg_list = list(jieba.cut(sentence, cut_all=False))
    return seg_list

# s_list = util.get_list_from_file(r"D:\semantic analysis\纯文本\常用词\美好//2011-09-03.txt")
# # 结巴分词词典的目录
# jieba.set_dictionary("D:\semantic analysis\分词\词库\导出结果\dict1.txt")
# jieba.initialize()
# r_list = []
# for sentence in s_list:
#     w_list = get_word_list(sentence)
#     r_list.append(("|").join(w_list))
# util.save_file(r"D:\semantic analysis\2016-10-09结果//分词测试.txt",r_list)


with open("tfc","r",encoding="utf-8") as f:
    s = f.readline()

print(util.input_filer(s))
print(",".join(util.input_filer(s)))
s = ",".join(util.input_filer(s))
s = ',' + s + ','
print(zky(s))
