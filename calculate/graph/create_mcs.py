# 创建最大公共连通子图
#  maximal common subgraph
import tool.util as util
import networkx as nx
import os
import copy


# 生成最大公共连通子图
def mcs(g2, g1):
    g2 = copy.deepcopy(g2)
    g1 = copy.deepcopy(g1)
    s1 = set(g2.edges())
    s2 = set(g1.edges())
    # 对称差集运算（项在t或s中，但不会同时出现在二者中）
    s3 = s1 ^ s2
    g2.remove_edges_from(s3)
    g1.remove_edges_from(s3)
    g1 = nx.algorithms.intersection(g2, g1)

    # 不连通的时，选取最大连通子图
    if ~nx.is_connected(g1):
        graph_list = list(nx.nx.connected_component_subgraphs(g1))
        c_list = []
        for cl in graph_list:
            c_list.append(cl.number_of_nodes())
        m = max(c_list)
        ii = c_list.index(m)
        g1 = graph_list[ii]

    return g1


def mcs_ratio(mcsg, cg, key):
    mn = len(list(nx.all_neighbors(mcsg, key)))
    # print(list(nx.all_neighbors(mcsg, key)))
    # print(mn)
    # print(list(nx.all_neighbors(cg, key)))
    cn = len(list(nx.all_neighbors(cg, key)))
    # print(cn)
    return mn/cn


# g2,g1 为两个待求的网络
# 返回 g1/g2 的比值
def mcs_ratio_advanced(g2, g1, key):
    m1 = set(nx.all_neighbors(g2, key))
    m2 = set(nx.all_neighbors(g1, key))
    m3 = m1 & m2
    return len(m3)/len(m1), len(m3)








    # 计算最大公共子图的比率
# pkl_dir: pkl 所在的目录
# mcs_dir: 结果生成的目录
# is_front: 是否跟前面的比较
# key_word：关键词
# lap： 步长
def cal_mcs(pkl_dir, mcs_dir, is_front, key_word, lap=1):
    f_list = util.get_file_list(pkl_dir, '.pkl')
    os.chdir(pkl_dir)
    # 升序排序
    nw_list = sorted(f_list)

    record_list = []
    num_list = []
    enum_list = []
    ii = len(nw_list)-1
    # g2是2号 g1是1号,此处获取最末端的网络
    g2 = util.get_nw(nw_list[ii])

    # 迭代生成子图
    k = 1
    while k < lap:
        g2 = mcs(g2, util.get_nw(nw_list[ii-k]))
        k += 1

    while ii > 0:
        jj = ii
        ii -= lap
        # print(nw_list[ii])

        g1 = util.get_nw(nw_list[ii])
        # 迭代生成子图
        k = 1
        while k < lap:
            g1 = mcs(g1, util.get_nw(nw_list[ii - k]))
            k += 1

        # 生成连通子图
        g1 = mcs(g2, g1)

        # 生成文件名字
        filename = nw_list[ii][0:-4] + '-' + nw_list[jj][0:-4] + '.pkl'

        # 2016.9.20 用于测试，保存结果
        util.save_nw(g1, 'D://semantic analysis//nalyze_data//result//过程结果//连通子图//' + filename)

        if is_front:
            # 计算比例，1，2  跟1比
            pr = mcs_ratio(g1, g1, key_word)
            record_list.append(nw_list[jj][0:-4] + '\t' + str(pr))
        else:
            # 计算比例，1，2  跟2比
            pr = mcs_ratio(g1, g2, key_word)
            record_list.append(nw_list[jj][0:-4] + '\t' + str(pr))

        num_list.append(nw_list[jj][0:-4] + '\t' + str(g1.number_of_nodes()))
        enum_list.append(nw_list[jj][0:-4] + '\t' + str(g1.number_of_edges()))

        # 统计节点数
        # with open(mcs_dir + filename[0:-4]+'.txt','w',encoding='utf-8') as file:
        #     for node in g1.nodes():
        #         file.write(node+'\n')
        # util.save_nw(g1,mcs_dir + filename)
        g2 = g1
    # util.save_file(mcs_dir + key_word+'mcs.txt', record_list)
    # util.save_file(mcs_dir + 'n' + key_word+'mcs.txt', num_list)
    # util.save_file(mcs_dir + 'e' + key_word+'mcs.txt', enum_list)


# 计算生成公共子图的节点数
def cal_node_mcs(pkl_dir, mcs_dir, key_word, lap=2):
    f_list = util.get_file_list(pkl_dir, '.pkl')
    os.chdir(pkl_dir)
    # 升序排序
    nw_list = sorted(f_list)
    record_list = []
    num_list = []
    enum_list = []
    ii = len(nw_list)-1

    while (ii-lap+1) >= 0:
        # print(nw_list[ii])
        g1 = util.get_nw(nw_list[ii])
        # 迭代生成子图
        k = 1
        while k < lap:
            g1 = mcs(g1, util.get_nw(nw_list[ii - k]))
            k += 1

        # 生成文件名字
        filename = nw_list[ii][0:-4] + '.pkl'

        # 保存结果
        pkl_dir = r"D:\semantic analysis\公共子图节点数\新词\30公共子图//" + key_word +"//"
        util.create_directory(pkl_dir)
        util.save_nw(g1, pkl_dir + nw_list[ii][0:-4])

        num_list.append(nw_list[ii][0:-4] + '\t' + str(g1.number_of_nodes()))
        enum_list.append(nw_list[ii][0:-4] + '\t' + str(g1.number_of_edges()))

        # 统计节点数
        # with open(mcs_dir + filename[0:-4]+'.txt','w',encoding='utf-8') as file:
        #     for node in g1.nodes():
        #         file.write(node+'\n')
        # util.save_nw(g1,mcs_dir + filename)

        ii -= lap

    # util.save_file(mcs_dir + key_word+'mcs.txt', record_list)
    util.save_file(mcs_dir + 'n' + key_word+'mcs.txt', num_list)
    util.save_file(mcs_dir + 'e' + key_word+'mcs.txt', enum_list)





# key_list = util.get_key_list()
# key_list = ['吐槽', '纠结', '自拍',  '美好']
# pkl_dir = 'D:\semantic analysis\新结果\共现网络//'
# mcs_dir = "D:\semantic analysis\公共子图节点数\新词//"

# 创建目录
# for key in key_list:
#     util.create_directory(mcs_dir+key)

# for key in key_list:
#     print(key)
#     ii = 30
#     while ii < 31:
#         print("-------"+str(ii)+"---------")
#         # 启动主函数,生成比例
#         # cal_mcs(pkl_dir+key+'//p', mcs_dir, True, key,1)
#         temp_dir = mcs_dir + '//' + str(ii) + '//'
#         util.create_directory(temp_dir)
#         cal_node_mcs(pkl_dir+key+'//p', temp_dir, key, ii)
#         ii += 1


# 倒叙生成子图后比较
def main1(keyword):
    dirr = 'D:\semantic analysis\pNet1\\' + keyword + '//p//'
    r_dir = 'D:\semantic analysis//3次采集结果\连续比例4//'
    pkl_list = util.get_file_list(dirr, '.pkl')
    pkl_list = sorted(pkl_list)
    for pkl in pkl_list:
        print(pkl)
    ll = len(pkl_list)-1
    ii = ll
    g = util.get_nw(dirr+'\\'+pkl_list[ii])
    r_list = []
    n_list = []

    # 生成五个图的公共子图
    while ii >= ll-3:
        ii -= 1
        g2 = util.get_nw(dirr+'\\'+pkl_list[ii])
        g = mcs(g2, g)
        print(pkl_list[ii]+'\t'+str(g.number_of_nodes()))

    ii = len(pkl_list)-1
    while ii > 0:
        ii -= 1
        g2 = util.get_nw(dirr + '\\' + pkl_list[ii])
        rr, nn = mcs_ratio_advanced(g2, g, keyword)
        r_list.append(pkl_list[ii][0:-4] + '\t' + str(rr))
        n_list.append(pkl_list[ii][0:-4] + '\t' + str(nn))
    util.save_file(r_dir+keyword+'.txt',r_list)
    util.save_file(r_dir + 'n'+keyword + '.txt', n_list)


# for key in key_list:
#     print(key)
#     main1(key)

# g2 = util.get_nw('D:\semantic analysis\c_date\给力\p//2011-03-31.pkl')
# g1 = util.get_nw('D:\semantic analysis\c_date\给力\p//2011-03-30.pkl')
# g1 = util.get_nw('D:\semantic analysis\c_date\给力\p//2011-03-29.pkl')
# g4 = util.get_nw('D:\semantic analysis\c_date\给力\p//2011-03-28.pkl')
#
#
# g5 = mcs(g2, g1)
# g6 = mcs(g1, g5)
# g7 = mcs(g4, g6)
# r = g1.number_of_nodes() / g2.number_of_nodes()
# print("的节点数："+str(g2.number_of_nodes()))
# print("的节点数："+str(g1.number_of_nodes()))
# print("两者公共子图的节点数："+str(g5.number_of_nodes()))
# print("两者公共子图的节点数："+str(g6.number_of_nodes()))
# print("两者公共子图的节点数："+str(g7.number_of_nodes()))

# print("比值1：" + str(g1.number_of_nodes() / g2.number_of_nodes()))
# print("比值2：" + str(g1.number_of_nodes() / g1.number_of_nodes()))