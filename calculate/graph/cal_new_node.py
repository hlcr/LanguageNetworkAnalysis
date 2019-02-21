# 计算新加入到原有网络的新节点的连接特性
import tool.util as util
import networkx as nx
import os


# 计算连接概率
# g2,g1 为两个待求的网络，g1前，g2后
def cal_connect_probability(g1, g2, key_word):
    s1 = set(g1.nodes())
    # 概率
    degree_set = set()
    sum_degree = 0
    for ori_word in s1:
        d = g1.degree(ori_word)
        sum_degree += d
        degree_set.add(d)

    result_dict = dict()
    for d in degree_set:
        result_dict[d] = d/sum_degree

    keys = list(result_dict.keys())
    keys.sort()
    result_list = list()
    for k in keys:
        result_list.append(str(k)+"\t"+str(result_dict.get(k, 0)))
    return result_list


# 计算新加入节点的特性 节点度
# g2,g1 为两个待求的网络，g1前，g2后
def cal_connect_real_probability(g1, g2, key_word):
    s1 = set(g1.nodes())
    s = set(g2.nodes()) - s1

    # 新网络中与新加入节点相连接的节点
    ori_list = list()
    for word in s:
        ori_list.extend(list(nx.all_neighbors(g2, word)))

    # 统计每个节点新连接的节点数
    node_num_dict = dict()

    for ori_node in ori_list:
        if ori_node in s1:
            node_num_dict[ori_node] = node_num_dict.get(ori_node, 0) + 1

    # 统计这些节点的概率
    total_num = sum(node_num_dict.values())
    for word, num in node_num_dict.items():
        node_num_dict[word] = num / total_num

    # 记录度与概率的关系
    degree_p_dict = dict()
    for word, num in node_num_dict.items():
        d = g1.degree(word)

        ll = degree_p_dict.get(d, list())
        ll.append(num)
        degree_p_dict[d] = ll

    # 计算平均值
    for word, ratio_list in degree_p_dict.items():
        degree_p_dict[word] = sum(ratio_list) / len(ratio_list)

    keys = list(degree_p_dict.keys())
    keys.sort()
    result_list = list()
    for k in keys:
        result_list.append(str(k)+"\t"+str(degree_p_dict.get(k, 0)))
    return result_list



# 计算新加入节点的特性 节点度
# g2,g1 为两个待求的网络，g1前，g2后
def extract_new_nodes_attributes(g1, g2, key_word):
    s1 = set(g1.nodes())
    s = set(g2.nodes()) - s1
    # 新网络中与新加入节点相连接的节点
    ori_list = list()
    for word in s:
        ori_list.extend(list(nx.all_neighbors(g2, word)))
    # 分布特性的结果字典
    result_dict = dict()
    for ori_node in ori_list:
        if ori_node in s1:
            d = g1.degree(ori_node)
            result_dict[d] = result_dict.get(d, 0) + 1
    keys = list(result_dict.keys())
    keys.sort()
    result_list = list()
    for k in keys:
        result_list.append(str(k)+"\t"+str(result_dict.get(k, 0)))
    return result_list


# 计算消失节点的特性 节点度
# g2,g1 为两个待求的网络，g1前，g2后
def extract_disappear_nodes_attributes(g1, g2, key_word):
    s = set(g1.nodes()) - set(g2.nodes())
    # 分布特性的结果字典
    result_dict = dict()
    for ori_node in s:
        d = g1.degree(ori_node)
        result_dict[d] = result_dict.get(d, 0) + 1
    keys = list(result_dict.keys())
    keys.sort()
    result_list = list()
    for k in keys:
        result_list.append(str(k)+"\t"+str(result_dict.get(k, 0)))
    return result_list


# 计算新加入节点的特性 节点度/节点数
# g2,g1 为两个待求的网络，g1前，g2后
def extract_new_nodes_attributes_ratio(g1, g2, key_word):
    s1 = set(g1.nodes())
    s = set(g2.nodes()) - s1
    s1.remove(key_word)
    # 新网络中与新加入节点相连接的节点
    ori_list = list()
    for word in s:
        ori_list.extend(list(nx.all_neighbors(g2, word)))
    # 分布特性的结果字典
    result_dict = dict()
    num_dict = dict()
    for ori_node in ori_list:
        if ori_node in s1:
            d = g1.degree(ori_node)
            ss = num_dict.get(d, set())
            ss.add(ori_node)
            num_dict[d] = ss
            result_dict[d] = result_dict.get(d, 0) + 1
    keys = list(result_dict.keys())
    keys.sort()
    result_list = list()
    for k in keys:
        result_list.append(str(k)+"\t"+str(result_dict.get(k, 0)/len(num_dict[k])))
    return result_list

# 计算新加入节点的特性 词频
# g2,g1 为两个待求的网络，g1前，g2后
word_freq_dict = util.get_nw(r"D:\semantic analysis\新结果\去虚词去单字\2017-4-9整理\词频分布\词频1.pkl")
def extract_new_nodes_attributes2(g1, g2, key_word):
    s1 = set(g1.nodes())
    s = set(g2.nodes()) - s1
    s1.remove(key_word)
    # 新网络中与新加入节点相连接的节点
    ori_list = list()
    for word in s:
        ori_list.extend(list(nx.all_neighbors(g2, word)))
    # 分布特性的结果字典
    result_dict = dict()
    for ori_node in ori_list:
        if ori_node in s1:
            d = word_freq_dict.get(ori_node, 0)
            result_dict[d] = result_dict.get(d, 0) + 1
    keys = list(result_dict.keys())
    keys.sort()
    result_list = list()
    for k in keys:
        result_list.append(str(k)+"\t"+str(result_dict.get(k, 0)))
    return result_list

# 计算新节点的特性
# pkl_dir: pkl 所在的目录
# mcs_dir: 结果生成的目录
# is_front: 是否跟前面的比较
# key_word：关键词
# lap： 步长
def loop_key(pkl_dir, result_dir, key_word, lap=1):
    pkl_dir = pkl_dir.format(key_word)
    f_list = util.get_file_list(pkl_dir, '.pkl')
    os.chdir(pkl_dir)
    # 升序排序
    nw_list = sorted(f_list)
    ii = len(nw_list)-1
    # g2是2号 g1是1号,此处获取最末端的网络
    g2 = util.get_nw(nw_list[ii])
    util.create_directory(result_dir + key_word)

    while ii > 0:
        jj = ii
        ii -= lap
        # print(nw_list[ii])
        g1 = util.get_nw(nw_list[ii])

        # 生成文件名字
        filename = nw_list[ii][0:-4] + '-' + nw_list[jj][0:-4] + '.txt'

        result_list = cal_connect_real_probability(g1, g2,key_word)
        util.save_file(result_dir + key_word + "//"+filename, result_list)

        g2 = g1


# 累计计算新节点的特性
# pkl_dir: pkl 所在的目录
# mcs_dir: 结果生成的目录
# is_front: 是否跟前面的比较
# key_word：关键词
# lap： 步长
def loop_key2(pkl_dir, result_dir, key_word, lap=1):
    pkl_dir = pkl_dir.format(key_word)
    f_list = util.get_file_list(pkl_dir, '.pkl')
    os.chdir(pkl_dir)
    # 升序排序
    nw_list = sorted(f_list)
    ii = 0
    # g2是2号 g1是1号,此处获取最末端的网络
    g1 = util.get_nw(nw_list[ii])
    util.create_directory(result_dir + key_word)

    while ii < len(nw_list)-lap:
        ii += lap
        g2 = util.get_nw(nw_list[ii])

        # 生成文件名字
        filename = nw_list[ii][0:-4] + '.txt'

        result_list = extract_new_nodes_attributes(g1, g2)
        util.save_file(result_dir + key_word + "//"+filename, result_list)
        g1 = nx.compose(g1, g2)


if __name__ == '__main__':
    # word_list = util.get_list_from_file(r"D:\semantic analysis\新结果\去虚词去单字\2017-4-9整理\词频分布\词频1.txt")
    # word_freq_dict = dict()
    # for word in word_list:
    #     item = word.split('\t')
    #     word_freq_dict[item[0]] = float(item[1])
    # util.save_nw(word_freq_dict, "词频1.pkl")

    keyword_list = util.get_key_list() + util.get_key_list2()
    for k in keyword_list:
        print(k)
        loop_key("D:\semantic analysis\新结果\去虚词去单字\合成共现网络\{0}\p//", "D:\semantic analysis\新结果\去虚词去单字//2017-4-9整理\新连接度分布特性度分布真实概率1//" , k, lap=1)
