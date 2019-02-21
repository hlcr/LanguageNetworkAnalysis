import networkx as nx
import os
import jieba
import pickle
import time
import tool.util as util



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
    seg_list = jieba.cut(sentence, cut_all=False)
    w_set = set(seg_list)
    w_set.discard(' ')
    return list(w_set)


# 把语句添加到已经存在的网络中,然后返回新图
def add_s2g(g, new_sentence):
    nw_list = get_word_list(new_sentence)
    g1 = create_graph(nw_list)
    return nx.compose(g, g1)


# 判断目录是否存在后建立目录
def mk_dir(s_dir):
    if not os.path.exists(s_dir):
        os.mkdir(s_dir)


def main():
    k_list = util.get_key_list()
    jieba.set_dictionary("D:\semantic analysis\分词\词库\导出结果\dict1.txt")
    jieba.initialize()
    for key in k_list:
        print(key)
        file_list = util.get_file_list('D://semantic analysis//analyze_data//fc//'+key, ".txt")
        # 建立目录
        mk_dir('./w')
        mk_dir('./p')

        for n_file in file_list:
            s_list = util.get_list_from_file(n_file)
            # 过滤相同的语句，防止重复计算
            print(len(s_list))
            s_list = list(set(s_list))
            print(len(s_list))
            wg = nx.Graph()
            pg = nx.Graph()

            for sentence in s_list:
                # 创建整句话的网络
                ll = util.input_filer(sentence)
                wg = add_s2g(wg, ' '.join(ll))

                # 只创建关键词所在的分句的网络
                for ss in ll:
                    if (key in ss):
                        pg = add_s2g(pg, ss)

            pkl_name = n_file[:-4] + '.pkl'
            util.save_nw(pg, './/p//'+pkl_name)
            util.save_nw(wg, './/w//'+pkl_name)

            print(n_file)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

            with open('record.txt','a',encoding='utf-8') as rf:
                rf.write(n_file+'\n')



main()

# g = add_s2g(g, '总觉得有什么事一样')
#
# save_nw(g,'test_save.pkl')
# g1 = get_nw('test_save.pkl')


