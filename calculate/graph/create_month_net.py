# 把一个月的词汇网络全部合并
import util
import networkx as nx

# pkl_dir: pkl所在的目录
# mnt: 生成的图所存放的目录
def create_net(pkl_dir, mnt):
    pkl_file_list = util.get_file_list(pkl_dir, '.pkl')
    m_dict = {}

    # 按照年月来分类所有的文件
    for file_name in pkl_file_list:
        fm = file_name[0:7]
        # 获取
        mf_list = m_dict.get(fm, [])
        if mf_list is None:
            mf_list = [file_name]
        else:
            mf_list.append(file_name)
        m_dict[fm] = mf_list

    # 创建存放按照月份创建的pkl目录
    util.create_directory(mnt)
    # 合并一个月内的所有网络
    for (k, vl) in m_dict.items():
        mg = nx.Graph()
        print(k)
        for file in vl:
            g1 = util.get_nw(pkl_dir+file)
            mg = nx.compose(mg, g1)
        util.save_nw(mg, mnt+k)

key_list = util.get_key_list()
pkl_dir1 = 'D:\semantic analysis\c_date//'
mnt1 = 'D:\semantic analysis\mpkl//'
# for key in key_list:
#     util.create_directory(mnt1+key)

for key in key_list:
    print(key)
    create_net(pkl_dir1+key+'//p//', mnt1+key+'//p//')