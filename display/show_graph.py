import os
import pickle
from collections import OrderedDict

import networkx as nx

import tool.util as util



# 解决中文乱码问题
def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


# 展示图形
def show_nw(graph):
    set_ch()
    import matplotlib.pyplot as plt
    nx.draw(graph,pos=nx.spring_layout(graph),node_size=1000,with_labels=True)
    plt.show()


# 保存对象
def save_nw(g, file_name):
    with open(file_name, 'wb') as f:  # open file with write-mode
        pickle.dump(g, f)  # serialize and save object


# 获取已经保存的网络对象
def get_nw(file_name):
    with open(file_name, 'rb') as f:
        g = pickle.load(f)  # read file and build object
    return g

# g = get_nw(r"D:\semantic analysis\新结果\去虚词去单字\合成共现网络\常用词年份\2010网络.pkl")
g1 = get_nw(r"D:\semantic analysis\新结果\去虚词去单字\合成共现网络\常用词年份\2010-2012网络.pkl")
# g.remove_edges_from(g.selfloop_edges())
# g1.remove_edges_from(g1.selfloop_edges())
# g.remove_node("美好")
# g1.remove_node("美好")
print("边数")
# print(len(g.nodes()))
print(len(g1.edges()))
print(len(g1.nodes()))
# ngs = set(g.nodes())
# ngs1 = set(g1.nodes())
# ngs2 = ngs & ngs1

# print("节点数")
# print(len(ngs))
# print(len(ngs1))
#
# ngs = ngs - ngs2
#
# for n in ngs:
#     g.remove_node(n)
#
#
# ngs1 = ngs1 - ngs2
# init_edge = len(g1.edges())
# for n in ngs1:
#     # print(n)
#     g1.remove_node(n)
# extra_edge = len(g1.edges()) - init_edge
# print("去除节点数")
# print(len(ngs))
# print(len(ngs1))
#
# print("剩余节点数")
# ngs = set(g.nodes())
# ngs1 = set(g1.nodes())
# print(len(ngs))
# print(len(ngs1))
#
# g2 = nx.difference(g1, g)
# print("相差的节点数和边数")
# print(len(g2.nodes()))
# print(len(g2.edges()))
# print((len(g2.edges())+init_edge) / (len(g1.edges())+init_edge))


# print(g.number_of_nodes())
# s = set(nx.k_shell(g).nodes())
# print(len(s))
# print(nx.k_shell(g).nodes())
# print(nx.k_shell(g1).nodes())
# cg  = nx.core_number(g)
# max_num = max(cg.values())
#
# print(max_num)
# show_nw(nx.k_shell(g))
# max_num = nx.core_number(g)
#
# print(max_num["男士"])
# for k in range(max_num+1):
#     print(k,end="\t")
#     print(nx.k_shell(g,k).number_of_nodes())

# print(len(nx.k_shell(g).nodes()))
# print(len(g.nodes()))
# kg = nx.k_shell(g)
# show_nw(kg)

# for node in kg.nodes():
#     print(node, end="\t")
#     print(len(g.neighbors(node)))
#     # print(nx.degree(node))

# print(g.degree())
# show_nw(kg)
# g = get_nw('D:\semantic analysis//analyze_data//fc\淡定\w1//2010-01-03.pkl')
# show_nw(g)

# ll = util.get_key_list()
# for w in ll:
#     print(w+' 3')
