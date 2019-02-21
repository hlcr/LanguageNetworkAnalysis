import tool.util as util
import os

key_list = util.get_key_list2()

for keyword in key_list:
    print(keyword)
    dirr = 'D:\semantic analysis\常用词的分词集合\\' + keyword
    os.chdir(dirr)
    pkl_list = util.get_file_list(dirr, '.pkl')
    pkl_list = sorted(pkl_list)
    util.create_directory(r"D:\semantic analysis\2016-10-05结果//"+keyword)
    i = 0
    s = util.get_nw(pkl_list[0])
    while i < len(pkl_list):
        s1 = util.get_nw(pkl_list[i]) | s
        s2 = s1 - s
        print(len(s2))
        util.save_nw(s2, r"D:\semantic analysis\2016-10-05结果//"+keyword+"//"+pkl_list[i])
        s = s1
        i += 1
