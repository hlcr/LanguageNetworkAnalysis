import tool.util as util

l1 = util.get_list_from_file(r"D:\semantic analysis\纯文本\1新词\扯淡\2014-05-15.txt")
l2 = util.get_list_from_file(r"D:\semantic analysis\纯文本\新词\扯淡\2014-05-15.txt")
l3 = set(l2)-set(l1)
for s in l3:
    print(s)