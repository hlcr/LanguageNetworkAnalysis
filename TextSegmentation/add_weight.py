# 用于对新词添加权重
import util

slist = util.get_list_from_file('D://semantic analysis//分词//词库//ok//result_dict.txt')

rlist = []
for ll in slist:
    rlist.append(ll + ' 3')

util.save_file('D://semantic analysis//分词//词库//ok//result_dict1.txt',rlist)