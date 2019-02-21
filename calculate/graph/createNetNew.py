# 用自己定义的数据结构创建图
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


# 获取分词的list
def get_word_list(sentence):
    # seg_list = jieba.cut(sentence, cut_all=False)
    # w_set = set(seg_list)
    # w_set.discard(' ')
    seg_list = pynlpir.segment(sentence, pos_tagging=False)
    return list(seg_list)


# 把语句添加到已经存在的网络中,然后返回新图
def add_s2g(g, new_sentence):
    nw_list = get_word_list(new_sentence)
    g1 = create_graph(nw_list)
    return nx.compose(g, g1)


# 判断目录是否存在后建立目录
def mk_dir(s_dir):
    if not os.path.exists(s_dir):
        os.mkdir(s_dir)


# 所有句子分句，并且生成矩阵
def create_matrix(s_list, keyword, is_all=False):
    # 存放所有分句分词后的结果
    ps_list = []
    pps_list = []
    # 存放所有分词结果
    ps_set = set()
    pps_set = set()
    for sentence in s_list:
        # 过滤并把一个句子切成分句
        spl = util.input_filer(sentence)
        for sp in spl:
            swl = get_word_list(sp)
            # 获取所有的分词结果
            for s in swl:
                ps_set.add(s)
            ps_list.append(swl)

            # 关键词所在的分句获取
            if keyword in sp:
                # 打印分句
                # print(sp)
                pswl = get_word_list(sp)
                # 打印分词结果
                # for ss in pswl:
                #     print(ss,end=',')
                # print('')
                # print('')
                # 获取所有的分词结果
                for s in pswl:
                    pps_set.add(s)
                pps_list.append(swl)
    if is_all:
        return ps_list, nxt.MatrixNetwork(list(ps_set)), pps_list, nxt.MatrixNetwork(list(pps_set))
    else:
        return pps_list, nxt.MatrixNetwork(list(pps_set))

from ctypes import c_char_p
def main():
    # 设置结果保存的目录
    result_dir = r'D:\semantic analysis\新结果\共现网络//'
    txt_dir = r"D:\semantic analysis\新纯文本\1常用词//"
    # k_list = util.get_key_list()
    # k_list = ['不约而同', '喜闻乐见', '努力', '感觉', '简单', '无聊', '希望', '美好']
    # 中心词
    k_list = ['美好']
    # 结巴分词词典的目录
    # jieba.set_dictionary("D:\semantic analysis\分词\词库\导出结果\dict1.txt")
    # jieba.initialize()
    pynlpir.open()
    for key in k_list:
        print(key)
        pynlpir.nlpir.AddUserWord(c_char_p(key.encode()))

    for key in k_list:
        print(key)
        # 文件目录
        file_list = util.get_file_list(txt_dir+key, ".txt")
        # 建立目录
        mk_dir(result_dir + key)
        # mk_dir(result_dir+key+'//w')
        mk_dir(result_dir+key+'//p')

        for n_file in file_list:
            s_list = util.get_list_from_file(txt_dir+key+"//"+n_file)
            # 过滤相同的语句，防止重复计算
            print(len(s_list))
            s_list = list(set(s_list))
            print(len(s_list))

            # 生成所有句子的网络
            # ps_list, mn, pps_list,pmn = create_matrix(s_list,key)
            pps_list,pmn = create_matrix(s_list,key)

            pkl_name = n_file[:-4] + '.pkl'

            # for w_list in ps_list:
            #     # 创建整句话的网络
            #     mn.add_edges(w_list)
            # util.save_nw(mn.get_network(), result_dir+key+'//w//' + pkl_name)

            for w_list in pps_list:
                # pmn.add_edges(w_list)
                pmn.add_gram_edges(w_list)
            util.save_nw(pmn.get_network(), result_dir+key+'//p//' + pkl_name)

            print(n_file)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

            with open(result_dir+key+'//record.txt','a',encoding='utf-8') as rf:
                rf.write(n_file+'\n')
    pynlpir.close()


main()