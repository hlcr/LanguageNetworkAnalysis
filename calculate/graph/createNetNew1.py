# 用自己定义的数据结构创建图,去掉虚词
import networkx as nx
import copy
import os
# import jieba
import pynlpir
import pickle
import time
import tool.util as util
import calculate.graph.network_tool as nxt

# 根据list来创建一个图对象
def create_graph(g_list):
    g = nx.Graph()
    i = len(g_list)
    j = i
    while i > 0:
        i -= 1
        j = i
        while j > 0:
            j -= 1
            g.add_edge(g_list[i],g_list[j])
    return g





# 所有句子分句，并且生成矩阵
def create_matrix(s_list, keyword):
    # 存放所有分句分词后的结果
    pps_list = []
    # 存放所有分词结果
    pps_set = set()
    for sentence in s_list:
        # 获取分词集合
        spl = util.get_word_list(sentence, keyword)
        for sp in spl:
            for s in sp:
                pps_set.add(s)
            pps_list.append(sp)
    return pps_list, nxt.MatrixNetwork(list(pps_set))

from ctypes import c_char_p
def main():
    # 设置结果保存的目录
    result_dir = r'D:\semantic analysis\新结果\去虚词去单字共现网络//'
    txt_dir = r"D:\semantic analysis\新纯文本\1常用词//"
    # k_list = util.get_key_list()
    # k_list = ['不约而同', '喜闻乐见', '努力', '感觉', '简单', '无聊', '希望', '美好']
    # 中心词
    k_list = ['希望', '气质', '害怕', '喜欢']

    # 结巴分词词典的目录
    # jieba.set_dictionary("D:\semantic analysis\分词\词库\导出结果\dict1.txt")
    # jieba.initialize()
    pynlpir.open()
    for key in k_list:
        pynlpir.nlpir.AddUserWord(c_char_p(key.encode()))

    for key in k_list:
        print(key)
        # 文件目录
        file_list = util.get_file_list(txt_dir+key, ".txt")
        # 建立目录
        util.create_directory(result_dir + key)
        # mk_dir(result_dir+key+'//w')
        util.create_directory(result_dir+key+'//p')

        for n_file in file_list:
            s_list = util.get_list_from_file(txt_dir+key+"//"+n_file)
            # 过滤相同的语句，防止重复计算
            print(len(s_list))
            s_list = list(set(s_list))
            print(len(s_list))

            # 生成所有分句的网络
            pps_list,pmn = create_matrix(s_list,key)

            pkl_name = n_file[:-4] + '.pkl'

            for w_list in pps_list:
                pmn.add_gram_edges(w_list)
            g = pmn.get_network()
            g.remove_edges_from(g.selfloop_edges())
            util.save_nw(g, result_dir+key+'//p//' + pkl_name)

            print(n_file)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

            with open(result_dir+key+'//record.txt','a',encoding='utf-8') as rf:
                rf.write(n_file+'\n')
    pynlpir.close()


main()

# s_list = util.get_list_from_file(r"D:\semantic analysis\新纯文本\1常用词\美好//2010-06-03.txt")
# pynlpir.open()
# keyword = "美好"
# pynlpir.nlpir.AddUserWord(c_char_p(keyword.encode()))
# for s in s_list:
#     print(get_word_list(s,"美好"))