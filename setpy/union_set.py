import tool.util as util


dir = r"D:\semantic analysis\常用词的分词集合\感觉\\"
set_list = sorted(util.get_file_list(dir,"pkl"))
# for file in set_list:
#     print(len(util.get_nw(dir+file)))
i = 0
r_set0 = set()
while i < len(set_list):
    r_set0 = r_set0 | util.get_nw(dir+set_list[i])
    print(len(r_set0))
    i += 1
#
# r_set = set()
# while i < 200:
#     r_set = r_set | util.get_nw(dir+set_list[i])
#     i += 1
#
# r_set2 = set()
# while i < 210:
#     r_set2 = r_set2 | util.get_nw(dir+set_list[i])
#     i += 1
#
# r_set3 = r_set & r_set2 & r_set0
# print(len(r_set0))
# print(len(r_set))
# print(len(r_set2))
# print(len(r_set3))
# util.save_nw(r_set3, r"D:\semantic analysis\2016-10-03结果\达人//上升集合2.pkl")

