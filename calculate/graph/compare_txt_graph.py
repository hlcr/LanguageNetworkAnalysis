from collections import OrderedDict

import tool.util as util
import networkx as nx
import os
import copy
from collections import Counter

def get_speical_dict(w_dict):
    r_dict = OrderedDict()
    index = 0
    stop_value = 0
    for k,v in w_dict.items():
        if v == 1 or v < stop_value:
            break
        r_dict[k] = v
        index += 1
        if index == 50:
            stop_value = v
    return r_dict


def get_txt_dict(txt_dir):
    w_list = util.get_list_from_file(txt_dir)
    w_dict = util.txt2dict(w_list)
    return get_speical_dict(w_dict)


def get_core_graph(pkl_dir):
    g = util.get_nw(pkl_dir)
    return nx.k_core(g)


def compare_function(dd,gg):
    s1 = set(dd.keys())
    s2 = set(gg.nodes())
    s3 = s1 & s2
    # print(len(s1))
    return str(len(s1)) + "\t" +str(len(s2)) + "\t" +str(len(s3))

# 计算最大公共子图的比率
# pkl_dir: pkl 所在的目录
# mcs_dir: 结果生成的目录
# is_front: 是否跟前面的比较
# key_word：关键词
# lap： 步长
def loop_compare(keyword_list, pkl_dir1, txt_dir1,result_dir, mode=1, lap=1):
    for key in keyword_list:
        print(key)
        if mode == 0:
            util.create_directory(result_dir + key + "//")
        
        pkl_dir = pkl_dir1.format(key)
        txt_dir = txt_dir1.format(key)
        
        # 获取日期列表
        d_list = util.get_file_list(pkl_dir, '.pkl')
        d_list = [d.split(".")[0] for d in d_list]
        
        result_list = []
        # 升序排序
        d_list = sorted(d_list)
        ii = len(d_list)-1

        while ii - lap >= 0:
            g1 = get_core_graph(pkl_dir + d_list[ii]+".pkl")
            d1 = get_txt_dict(txt_dir + d_list[ii]+".txt")

            # 迭代生成子图
            k = 1
            while k < lap:
                g1 = nx.compose(g1, util.get_nw(d_list[ii - k]))
                k += 1
            result_list.append(compare_function(d1, g1))
            ii -= lap
        util.save_file(result_dir + key + ".txt", result_list)


key_word_list = ["美好","努力","无聊"]
loop_compare(key_word_list, "D:\semantic analysis\新结果\去虚词去单字共现网络\{0}\p//", "D:\semantic analysis\新结果\去重去虚词去单字词频数\{0}//","D:\semantic analysis\新结果\去虚词去单字k-core词频保留比例//")