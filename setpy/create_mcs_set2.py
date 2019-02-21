import os
import tool.util as util


def cal_mcs(pkl_dir):
    os.chdir(pkl_dir)
    pkl_list = util.get_file_list(pkl_dir, '.pkl')
    # 从小到大排序
    pkl_list = sorted(pkl_list)

    m_set = util.get_nw(r"D:\semantic analysis\2016-10-03结果\达人//上升集合1.pkl")
    for file in pkl_list:
        set1 = util.get_nw(file)
        r_set = m_set & set1
        print(len(r_set)/len(m_set))


cal_mcs("D:\semantic analysis\分词集合\达人//")