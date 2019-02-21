import tool.util as util
import networkx as nx
import xlsxwriter
import copy
import numpy as np
import os


def calculate_attribute(result_list):
    array_list = copy.deepcopy(result_list)
    array_list.pop(0)
    average_list = []
    var_list = []
    col_num = len(array_list[0])-1
    m = np.array(array_list)
    for col in range(0, col_num):
        average_list.append(util.average(m[:, col]))
        var_list.append(util.variance(m[:, col]))

    c_num = 0
    for v in var_list:
        if v < 1.5:
            c_num += 1
    var_list.append(c_num)
    var_list.append(c_num/len(var_list))
    print(c_num)
    print(c_num/len(var_list))
    result_list.append(average_list)
    result_list.append(var_list)


def create_excel(workbook, data_list, table_name):
    worksheet = workbook.add_worksheet(table_name)
    for i, row in enumerate(data_list):
        worksheet.write_row(i, 0, row)
        # for j, item in enumerate(row):
        #     c1 = chr(65 + j)
        #     worksheet.write_row(i,j, row)


def cal_all_k_shells(g):
    max_num = max(nx.core_number(g).values())
    print(max_num)
    for k in range(max_num+1):
        print(k,end="\t")
        print(nx.k_shell(g,k).number_of_nodes())


def loop_compare(init_graph, file_dir):
    file_list = util.get_obj_list(file_dir,".pkl")[index:]
    result_list = []
    node_list = list(nx.k_core(init_graph).nodes())
    result_list.append(node_list)
    for graph in file_list:
        temp_list = []
        core_num_dict = nx.core_number(graph)
        max_num = max(core_num_dict.values())
        for node in node_list:
            temp_list.append(max_num+1 - core_num_dict.get(node, max_num+1))
        temp_list.append(max_num)
        result_list.append(temp_list)
    result_list[0].append("总层数")
    return result_list

index = 0
if __name__ == '__main__':
    keyword_list = util.get_key_list2() + util.get_key_list()
    # keyword_list = ["纠结"]
    workbook = xlsxwriter.Workbook("D:\semantic analysis\新结果\去虚词去单字/kcore共现网络变化整体{0}.xlsx".format(str(index)))

    for keyword in keyword_list:
        dd = "D:\semantic analysis\新结果\去虚词去单字\共现网络\{0}\p//".format(keyword)
        i_file = r"D:\semantic analysis\新结果\去虚词去单字\总网络\{0}\p//".format(keyword)
        i_f = util.get_file_list(i_file,".pkl")[0]
        nn = util.get_file_list(dd,".pkl")[index]
        print(keyword)
        ig = util.get_nw(i_file+i_f)
        rl = loop_compare(ig, dd)
        calculate_attribute(rl)
        create_excel(workbook, rl, keyword)
    workbook.close()

