import tool.util as util
import networkx as nx
import os
import copy
from collections import OrderedDict
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


def calculate_existed_ratio(g1, g2, d1):
    gg = get_speical_dict(g1)
    s1 = set(gg.keys())
    # s1 = set(gg.keys()) & set(nx.k_core(d1).nodes())
    s2 = set(g2.keys())
    s3 = s1 & s2
    # return str(len(s1))+"\t"+str(len(s3))
    if len(s1) == 0:
        return 0
    return str(len(s3)/len(s1))

# 计算最大公共子图的比率
# pkl_dir: pkl 所在的目录
# mcs_dir: 结果生成的目录
# is_front: 是否跟前面的比较
# key_word：关键词
# lap： 步长
def loop_compare(com_function, keyword_list, pkl_dir1, result_dir, mode=1, lap=1, type="pkl"):
    for key in keyword_list:
        print(key)
        if mode == 0:
            util.create_directory(result_dir + key + "//")
        pkl_dir = pkl_dir1.format(key)
        f_list = util.get_file_list(pkl_dir, '.txt')
        os.chdir(pkl_dir)
        result_list = []
        # 升序排序
        nw_list = sorted(f_list)
        ii = len(nw_list)-1

        while ii - 2*lap >= 0:
            g2 = util.txt2dict(util.get_list_from_file(nw_list[ii]))
            # 迭代生成子图
            k = 1
            while k < lap:
                g2 = nx.compose(g2, util.get_nw(nw_list[ii - k]))
                k += 1

            ii -= lap
            g1 = util.txt2dict(util.get_list_from_file(nw_list[ii]))
            d1 = util.get_nw("D:\semantic analysis\新结果\去虚词去单字共现网络//{0}//p//".format(key)+nw_list[ii].split(".")[0]+".pkl")
            # 迭代生成子图
            k = 1
            while k < lap:
                g1 = nx.compose(g1, util.get_nw(nw_list[ii - k]))
                k += 1

            # 生成连通子图
            if mode == 1:
                r1, r2 = com_function(copy.deepcopy(g1), copy.deepcopy(g2))
                result_list.append(nw_list[ii + lap][0:-4] + "\t" + str(r1))
                result_list.append((nw_list[ii][0:-4] + "\t" + str(r2)))
            elif mode == 0:
                result_list = com_function(copy.deepcopy(g1), copy.deepcopy(g2))
                util.save_file(result_dir + key + "//" + nw_list[ii + lap][0:-4] + ".txt", result_list)
            elif mode == 2:
                r1 = com_function(copy.deepcopy(g1), copy.deepcopy(g2), d1)
                # result_list.append(str(r1))
                result_list.append(nw_list[ii + lap][0:-4] + "\t" + str(r1))

            ii -= lap
        if mode != 0:
            result_list.reverse()
            util.save_file(result_dir+key+".txt", result_list)



key_list = ["美好","无聊"]
pkl_dir = r"D:\semantic analysis\新结果\去重去虚词去单字词频数\{0}//"
result_dir = r"D:\semantic analysis\新结果\去虚词去单字共现网络最大频率全图节点保留比例//"
loop_compare(calculate_existed_ratio, key_list, pkl_dir, result_dir, 2, 1)
# loop_compare(same_node_degree, key_list, pkl_dir, result_dir, 0)


