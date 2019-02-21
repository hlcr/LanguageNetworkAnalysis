import tool.util as util
import networkx as nx

file_path = "D:\semantic analysis\新结果\共现网络\{0}\p//"
result_path = "D:\semantic analysis\结果\度分布比率\{0}//"
# file_path = "D:\semantic analysis\分词网络\pNet\{0}\p//"
keyword_list = ["美好"]

for keyword in keyword_list:
    # 目前所在的路径
    cur_path = file_path.format(keyword)
    # 获取文件列表
    file_list = sorted(util.get_file_list(cur_path, ".pkl"))
    for file in file_list:
        item = file.split(".")[0]+ "\t"
        g = util.get_nw(cur_path+file)
        # 计算所有节点间平均最短路径长度
        item += str(nx.average_shortest_path_length(g))

        # 计算平均群聚系数
        item = item + "\t" + str(nx.average_clustering(g))

        # item = item + "\t" + str(nx.average_neighbor_degree(g))

        # item = item + "\t" + str(nx.average_degree_connectivity(g))

        item = item + "\t" + str(nx.diameter(g))
        # item = item + "\t" + str(nx.degree_centrality(g))

        print(item)
        # 所有度
        # degree_list = nx.degree_histogram(g)
        # degree_list = [z / float(sum(degree_list)) for z in degree_list]
        # print(g.degree())

        # degree_list.sort()
        # degree_list.reverse()
        # util.create_directory(result_path.format(keyword))
        # util.save_file(result_path.format(keyword)+"//"+file[:-4]+".txt", degree_list)


