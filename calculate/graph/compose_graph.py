from tool.util import *
import networkx as nx
import random

keyword_list = get_key_list2()
rg = nx.Graph()
r_dirr = r"D:\semantic analysis\新结果\去虚词去单字\合成共现网络\常用词年份//"
for key_word in keyword_list:
    dirr = r"D:\semantic analysis\新结果\去虚词去单字\总网络\{0}\p//".format(key_word)


    print(key_word)
    g_list = get_file_list(dirr, ".pkl")
    os.chdir(dirr)
    for i, g in enumerate(g_list):
        # if nn < len(g_list)-1:
        #     rg = nx.compose(rg, get_nw(g))
        #     nn += 1
        #     print(g)
        # else:
        #     save_nw(rg, r_dirr+g)
        #     nn = 0
        #     rg = get_nw(g_list[i])
        #     print("save")
        rg = nx.compose(rg, get_nw(g))
        print(g)

save_nw(rg, r_dirr+"总网络.pkl")
print("save")
        # print(len(get_nw(g).nodes()))