import datetime

import tool.util as util
import os

Num = 30


# txt_dirs：txt所在的目录列表
# xls_name: 输出文件名所在的目录
def create(txt_dirs, xls_name):
    data_dict = {}
    for txt_dir in txt_dirs:
        os.chdir(txt_dir)
        file_list = util.get_file_list(txt_dir, 'txt')
        for file in file_list:
            key = file[0:-4]
            data_list = util.get_list_from_file(file)
            x_list = []
            y_list = []
            for data in data_list:
                item = data.split('\t')

                x_list.append(datetime.datetime.strptime(item[0], '%Y-%m-%d'))
                y_list.append(float(item[1]))
            if key in data_dict.keys():
                data_dict[key] = data_dict[key] + [x_list]
                data_dict[key] = data_dict[key] + [y_list]
            else:
                data_dict[key] = [x_list,y_list]

    bl_list = []
    ii = Num - 1
    while ii < Num:
        ii += 1
        bl_list.append(str(ii))

    # util.create_xlsx(data_dict, bl_list, txt_dirs[0] + xls_name + '.xlsx')
    util.create_xlsx(data_dict, bl_list, xls_name )

# txt_dir = 'D://semantic analysis//3次采集结果//比例'
# i = 0
# while i != 3:
#     i += 1
#     create(txt_dir+str(i)+'//'+'比例', str(i))
#     create(txt_dir+str(i)+'//'+'边数', str(i))
#     create(txt_dir+str(i)+'//'+'节点数', str(i))


# dir_list = []
# dir_list2 = []
# jj = Num-1
# while jj < Num:
#     jj += 1
#     dir_list.append("D:\semantic analysis\公共子图节点数\常用词\\"+str(jj))
#     dir_list2.append("D:\semantic analysis\公共子图节点数\新词\\"+str(jj))
#
#
# create(dir_list,str(Num)+'节点数')
# create(dir_list2,str(Num) +  '节点数')

# create([r"D:\semantic analysis\2016-10-03结果\常用词\增量//"],r"D:\semantic analysis\2016-10-03结果\常用词增量.xlsx")
# create([r"D:\semantic analysis\2016-10-03结果\常用词\总量//"],r"D:\semantic analysis\2016-10-03结果\常用词总量.xlsx")
# create([r"D:\semantic analysis\2016-10-03结果\新词\增量//"],r"D:\semantic analysis\2016-10-03结果\新词增量.xlsx")
# create([r"D:\semantic analysis\2016-10-03结果\新词\总量//"],r"D:\semantic analysis\2016-10-03结果\信词总量.xlsx")
# create([r"D:\semantic analysis\2016-10-03结果\常用词\去掉前15个的比例//"],r"D:\semantic analysis\2016-10-03结果\常用词比例15.xlsx")
create([r"D:\semantic analysis\新结果\去虚词去单字\边保留概率//"],r"D:\semantic analysis\新结果\去虚词去单字\边保留概率\边比率.xlsx")
# create([r"D:\semantic analysis\新结果\去虚词去单字共现网络最大k-shell图节点保留比例11//"],r"D:\semantic analysis\新结果\去虚词去单字共现网络最大k-shell图节点保留比例11//比例.xlsx")