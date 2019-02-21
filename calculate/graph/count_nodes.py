# 统计所有子图的节点数
import tool.util as util
import networkx as nx


def count_num_of_node(pkl_dir):
    pkl_file_list = util.get_file_list(pkl_dir, '.pkl')
    r_list = []
    for file in pkl_file_list:
        g = util.get_nw(file)
        s = file[0:10] + '\t' + str(g.number_of_nodes())
        r_list.append(s)
    return r_list


key_list = util.get_key_list()
pkl_dir1 = r'D:\semantic analysis\pNet1//'
df_dir = r'D://semantic analysis//3次采集结果//节点数//'
# for key in key_list:
#     util.create_directory(df_dir+key)
for key in key_list:
    print(key)
    r = count_num_of_node(pkl_dir1+key+'//p//')
    util.save_file(df_dir+key+'.txt',r)