import networkx as nx
import tool.util as util
import os

dir = "D:\semantic analysis\新结果\去虚词去单字共现网络\纠结\p//"
os.chdir(dir)
file_list = util.get_file_list(dir,"pkl")
s1 = set()
l1 = list()


sg=util.get_nw(file_list[0])
for file in file_list[0:20]:
    g = util.get_nw(file)
    sg = nx.compose(g,sg)

gs = set(sg.nodes())
print("gs ",end=" ")
print(len(gs))
for file in file_list[0:20]:
    g = util.get_nw(file)
    s1 = s1 | set(nx.k_core(g).nodes())
    l1.extend(nx.k_core(g).nodes())


print("s1 " + str(len(s1)))
print("l1 " + str(len(l1)))

s2 = set()
l2 = list()
for file in file_list[-50:]:
    g = util.get_nw(file)
    s2 = s2 | set(nx.k_core(g).nodes())
    l2.extend(nx.k_core(g).nodes())

print("s2 "+str(len(s2)))
print("l2 " + str(len(l2)))

ss = s2 - gs
print(len(ss))
print(ss)

s3 = s1&s2
print(s3)
print(len(s3))