import networkx as nx
import os
import jieba
import pickle
import time
import util
import time



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

s_list = util.get_list_from_file('D:\semantic analysis\c_date\淡定//2011-07-30.txt')
# 过滤相同的语句，防止重复计算
print(len(s_list))
s_list = list(set(s_list))
print(len(s_list))
wg = nx.Graph()
pg = nx.Graph()
ii = 0
time_cost = []
# time_cost1 = []

print(time.strftime('%H:%M:%S', time.localtime(time.time())))

for sentence in s_list:
    # 创建整句话的网络
    ll = util.input_filer(sentence)

    start = time.clock()
    wg = add_s2g(wg, ' '.join(ll))
    end = time.clock()
    tc = str(end - start)
    ii += 1
    if ii == 50:
        ii = 0
        print(tc)
    time_cost.append(tc)
    # time_cost1.append(tc1)
    # 只创建关键词所在的分句的网络
    # for ss in ll:
    #     if ('淡定' in ss):
    #         pg = add_s2g(pg, ss)

print(time.strftime('%H:%M:%S', time.localtime(time.time())))

util.save_file('D:\semantic analysis\c_date/zw_record1.txt', time_cost)
