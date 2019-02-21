from tool.util import *
import networkx as nx
import math
from sklearn import linear_model
import numpy as np

global global_keyword

# 一个关键词生成一个文本结果文档
def calculate_attribute(p_function, s_parent_dir, s_type, r_file_dir):
    file_list = get_file_list(s_parent_dir, s_type)
    result_list = []
    for file in file_list:
        result = p_function(s_parent_dir, file)
        result_list.append(result)
    with open(r_file_dir, "w") as f:
        for result in result_list:
            f.write(str(result)+"\n")


# 一对一生成结果
def calculate_attributes(p_function, s_parent_dir, s_type, r_parent_dir):
    file_list = get_file_list(s_parent_dir, s_type)
    for file in file_list:
        result_list = p_function(s_parent_dir, file)
        with open(r_parent_dir+file.split(".")[0]+".txt", "w") as f:
            for result in result_list:
                f.write(str(result) + "\n")


# 循环关键词
def loop_key(keyword_list, mode, p_function, s_pattern_dir, s_type, r_file_dir):
    global global_keyword
    for key in keyword_list:
        global_keyword = key
        print(key)
        if mode == 0:
            calculate_attribute(p_function, s_pattern_dir.format(key), s_type, r_file_dir+key+".txt")
        else:
            # calculate_attributes(p_function, s_pattern_dir.format(key), s_type, r_file_dir + "//")
            create_directory(r_file_dir + key + "//")
            calculate_attributes(p_function, s_pattern_dir.format(key), s_type, r_file_dir + key + "//")


# 计算最大k-shell值
def calculate_max_k_core_num(s_parent_dir, file):
    g = get_nw(s_parent_dir+file)
    g.remove_edges_from(g.selfloop_edges())
    return file.split(".")[0]+"\t"+str(max(nx.core_number(g).values()))


# 计算最大k-core值里面的节点数
def calculate_max_k_core_node_num(s_parent_dir, file):
    g = get_nw(s_parent_dir+file)
    g.remove_edges_from(g.selfloop_edges())
    g = nx.k_core(g)
    return file.split(".")[0]+"\t"+str(g.number_of_nodes())


# 计算每层k-shell里面的节点数
def calculate_k_shell_node_num(s_parent_dir, file):
    r_list = []
    g = get_nw(s_parent_dir+file)
    g.remove_edges_from(g.selfloop_edges())
    max_num = max(nx.core_number(g).values())
    for k in range(max_num + 1):
        r_list.append(str(k)+"\t"+str(nx.k_shell(g, k).number_of_nodes()))
    del(r_list[0])
    r_list.reverse()
    return r_list

# 计算txt里句子的条数
def calculate_num_sentence(s_parent_dir, file):
    return file.split(".")[0] + "\t" + str(len(set(get_list_from_file(s_parent_dir+file))))

# 计算节点数
def calculate_num_node(s_parent_dir, file):
    g = get_nw(s_parent_dir + file)
    return file.split(".")[0] + "\t" + str(g.number_of_nodes())


# 计算度分布
def calculate_degree_histogram(s_parent_dir, file):
    g = get_nw(s_parent_dir + file)
    degree_list = nx.degree_histogram(g)
    s = float(sum(degree_list))
    degree_list = [z / s for z in degree_list]
    return degree_list


# 计算真实的平均路径长度
def average_shortest_path_length_real(s_parent_dir, file):
    global global_keyword
    g = get_nw(s_parent_dir + file)
    g.remove_node(global_keyword)
    g = max(nx.connected_component_subgraphs(g), key=len)
    rr = nx.average_shortest_path_length(g)
    print(rr)
    return rr

# 计算累计度分布
def calculate_accumulate_degree_histogram(s_parent_dir, file):
    degree_list = get_list_from_file(s_parent_dir+file)
    degree_list = [float(num.strip()) for num in degree_list]
    result_list =[]
    for index, item in enumerate(degree_list):
        result_list.append(str(sum(degree_list[index:])))
    return result_list

# 计算在双对数坐标下的度分布
def calculate_log_degree_histogram(s_parent_dir, file):
    degree_list = get_list_from_file(s_parent_dir+file)
    degree_list = [float(num.strip()) for num in degree_list]
    # 去掉关键词带来的尾巴
    degree_list.reverse()
    init_num = degree_list[0]
    for index, item in enumerate(degree_list):
        if item != init_num:
            degree_list = degree_list[index:]
            break
    degree_list.reverse()

    result_list =[]
    for index, item in enumerate(degree_list):
        result_list.append(str(math.log(index+1))+"\t"+str(math.log(item)))
    return result_list

# 计算双对数坐标下的斜率
def calculate_log_k(s_parent_dir, file):
    degree_list = get_list_from_file(s_parent_dir+file)
    x = []
    y = []
    for xy in degree_list:
        x.append(float(xy.split("\t")[0]))
        y.append(float(xy.split("\t")[1]))
    # 线性回归
    clf = linear_model.LinearRegression()
    # 训练
    clf.fit(np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1))
    return clf.coef_[0][0]

# 计算网络鲁棒性R值
def calculate_network_r(s_parent_dir, file):
    g = get_nw(s_parent_dir + file)
    g.remove_edges_from(g.selfloop_edges())
    # k_shell_dict = nx.core_number(g)
    k_shell_dict = g.degree()
    # 总节点数
    total_node_num = g.number_of_nodes()
    r_list = []
    ordered_k_shell_dict = OrderedDict(sorted(k_shell_dict.items(), key=lambda x: x[1], reverse=True))
    i = 0
    # print(m_num_node)
    for k, v in ordered_k_shell_dict.items():
        # i += 1
        # if i == m_num_node:
        #     # show_nw(g)
        #     break
        g.remove_node(k)
        sub_graphs = nx.connected_component_subgraphs(g)
        max_node_num = 0
        for j, sg in enumerate(sub_graphs):
            if sg.number_of_nodes() > max_node_num:
                max_node_num = sg.number_of_nodes()
        r_list.append(max_node_num/total_node_num)
        print(max_node_num/total_node_num)

    # print(r_list)
    result = sum(r_list)/total_node_num
    print(file.split(".")[0]+"\t"+str(result))
    return file.split(".")[0]+"\t"+str(result)


# 计算网络节点数
def calculate_network_node_num(s_parent_dir, file):
    g = get_nw(s_parent_dir + file)
    return file.split(".")[0]+"\t"+str(g.number_of_nodes())




file_dir = "D:\semantic analysis\新结果\去虚词去单字\合成共现网络//{0}\p//"
kl = get_key_list()
kl.reverse()
keyword_list = kl+get_key_list2()

# file_dir = "D:\semantic analysis\新结果\度分布\{0}//"
# loop_key(keyword_list,  0, calculate_network_node_num, file_dir, ".pkl","D:\semantic analysis\新结果\去虚词去单字节点数//")
# loop_key(keyword_list,  calculate_attribute, calculate_max_k_core_node_num, file_dir, ".pkl","D:\semantic analysis\新结果\最大k-core节点数//")
# loop_key(keyword_list,  0, calculate_max_k_core_num, file_dir, ".pkl","D:\semantic analysis\新结果\去虚词去单字\共现网络\最大k-core值//")
# loop_key(keyword_list,  1, calculate_k_shell_node_num, file_dir, ".pkl", "D:\semantic analysis\新结果\去虚词去单字\总网络的每层shell节点数量//")
# loop_key(keyword_list,  1, calculate_degree_histogram, file_dir, ".pkl", "D:\semantic analysis\新结果\去虚词去单字\整月网络度分布//")
# loop_key(keyword_list,  1, calculate_accumulate_degree_histogram, "D:\semantic analysis\新结果\去虚词去单字\整月网络度分布\{0}//", ".txt", "D:\semantic analysis\新结果\去虚词去单字\整月网络累计度分布//")
# loop_key(keyword_list,  1, calculate_log_degree_histogram, "D:\semantic analysis\新结果\去虚词去单字\整月网络累计度分布//{0}//", ".txt", "D:\semantic analysis\新结果\去虚词去单字\整月网络累计度分布（双对数坐标）//")
# loop_key(keyword_list,  0, calculate_log_k, r"D:\semantic analysis\新结果\去虚词去单字\2017-4-9整理\新连接度分布特性度分布比率//{0}//", ".txt", r"D:\semantic analysis\新结果\去虚词去单字\2017-4-9整理\新连接度分布特性度分布比率斜率//")
# loop_key(keyword_list,  0, calculate_num_node, "D:\semantic analysis\新结果\去虚词去单字\合成共现网络//{0}//p//", ".pkl", "D:\semantic analysis\新结果\去虚词去单字//2017-4-7整理\节点数//")
loop_key(keyword_list,  0, average_shortest_path_length_real, "D:\semantic analysis\新结果\去虚词去单字\合成共现网络//{0}//p//", ".pkl", r"D:\semantic analysis\新结果\去虚词去单字\2017-4-9整理\平均路径长度//")

# file_dir = r"D:\semantic analysis\新纯文本\1新词\{0}//"
# loop_key(keyword_list,  calculate_attribute, calculate_num_sentence, file_dir, ".txt","D:\semantic analysis\新结果\去重句子数\新词//")

# http://networkx.readthedocs.io/en/networkx-1.11/reference

# calculate_network_r("D:\semantic analysis\新结果\共现网络\吐槽\p//", "2013-06-13.pkl")
