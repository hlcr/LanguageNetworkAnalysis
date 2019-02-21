# 计算节点的比例数值
# 日期    数量
import tool.util as util

file_list = util.get_file_list('D:\semantic analysis//3次采集结果\节点数','.txt')

for f in file_list:
    x_list = []
    y_list = []
    ry_list = []
    r_data_list = []
    data_list = util.get_list_from_file(f)
    for data in data_list:
        item = data.split('\t')
        x_list.append(item[0])
        y_list.append(float(item[1]))

    my = max(y_list)
    i = 0
    while i < len(x_list):
        r_data_list.append(x_list[i] + '\t' + str(y_list[i]/my))
        i += 1
    util.save_file('D:\semantic analysis//3次采集结果\节点数'+'//'+f[0:-4]+'mcs.txt',r_data_list)



