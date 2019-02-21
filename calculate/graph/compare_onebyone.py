import tool.util as util
import networkx as nx
import os
import copy
from collections import Counter


def variance(l):  # 平方-期望的平方的期望
    ex = float(sum(l)) / len(l)
    s = 0
    for i in l:
        s += (i - ex) ** 2
    return float(s) / len(l)


# 计算最大k-core保留比例
def max_k_shell(g1, g2):
    g2 = nx.k_core(g2)
    g1 = nx.k_core(g1)

    s1 = set(g1.nodes())
    s2 = set(g2.nodes())
    s3 = s1 & s2

    print(str(len(s3)/len(s1)))
    print(str(len(s3)/len(s2)))
    return len(s3)/len(s1), len(s3)/len(s2)


# 计算共同节点数在两个图之间的度分布
def same_node_degree(g1, g2):
    g2.remove_edges_from(g2.selfloop_edges())
    g1.remove_edges_from(g1.selfloop_edges())
    s1 = set(g1.nodes())
    s2 = set(g2.nodes())
    s3 = s2 - s1
    ns_list = []
    temp_list = []
    for node in s3:
        ns1 = g2.neighbors(node)
        cc = 0
        for n in ns1:
            if n in s1:
                cc += 1
        ns_list.append(cc)
        if cc == 5:
            temp_list.append(node)
    dd = nx.core_number(g2)
    tt_list = []
    for temp_word in temp_list:
        tt_list.append(dd[temp_word])
    if len(tt_list) > 0:
        print(len(tt_list),end="\t")
        print(sum(tt_list)/len(tt_list),end="\t")
        print(variance(tt_list))
    r_dict = Counter(ns_list)
    r_list = list(range(max(r_dict.keys())+1))
    for k,v in r_dict.items():
        r_list[k] = v
    return r_list


def calculate_existed_ratio(g1, g2):
    gg = nx.k_core(g1)
    s1 = set(gg.nodes())
    s2 = set(nx.k_core(g2).nodes())
    s3 = s1 & s2
    # return str(len(s1)) + "\t" + str(len(s3))
    return str(len(s3)/len(s1))

# 计算最大公共子图的比率
# pkl_dir: pkl 所在的目录
# mcs_dir: 结果生成的目录
# is_front: 是否跟前面的比较
# key_word：关键词
# lap： 步长
def loop_compare(com_function, keyword_list, pkl_dir1, result_dir, mode=1, lap=1, type="pkl"):
    for keyword in keyword_list:
        pkl_dir = pkl_dir1.format(keyword)
        f_list = util.get_file_list(pkl_dir, '.pkl')
        os.chdir(pkl_dir)
        # 升序排序
        nw_list = sorted(f_list)

        record_list = []
        ii = len(nw_list)-1
        # g2是2号 g1是1号,此处获取最末端的网络
        g2 = util.get_nw(nw_list[ii])

        # 迭代生成子图
        k = 1
        while k < lap:
            g2 = nx.compose(g2, util.get_nw(nw_list[ii-k]))
            k += 1

        while ii-lap >= 0:
            jj = ii
            ii -= lap
            # print(nw_list[ii])

            g1 = util.get_nw(nw_list[ii])
            # 迭代生成子图
            k = 1
            while k < lap:
                g1 = nx.compose(g1, util.get_nw(nw_list[ii - k]))
                k += 1


            # 计算比例
            r1 = com_function(g1, g2)
            record_list.append(nw_list[jj][0:-4] + '\t' + str(r1))

            g2 = g1
        record_list.reverse()
        util.save_file(result_dir + keyword + ".txt", record_list)



key_list = util.get_key_list2()
pkl_dir = r"D:\semantic analysis\新结果\去虚词去单字共现网络\{0}\p//"
# pkl_dir = r"D:\semantic analysis\新结果\合并图\{0}//"
result_dir = r"D:\semantic analysis\新结果\去虚词去单字\k-core保留//"
# result_dir = r"D:\semantic analysis\新结果\合并图\扯淡//"
loop_compare(calculate_existed_ratio, key_list, pkl_dir, result_dir, 2, 1)
# loop_compare(same_node_degree, key_list, pkl_dir, result_dir, 0)


