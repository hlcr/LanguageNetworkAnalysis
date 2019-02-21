import tool.util as util
import os

# key_list = util.get_key_list2()
#
# for keyword in key_list:
#     print(keyword)
#     dirr = 'D:\semantic analysis\分词网络\pNet2\\' + keyword + '//p//'
#     os.chdir(dirr)
#     pkl_list = util.get_file_list(dirr, '.pkl')
#     util.create_directory(r"D:\semantic analysis\常用词的分词集合//"+keyword)
#     for pkl in pkl_list:
#         g = util.get_nw(pkl)
#         s = set(g.nodes())
#         util.save_nw(s,r"D:\semantic analysis\常用词的分词集合//"+keyword+"//"+pkl)



# 测试数据
util.save_nw(set(["我们","你们","他们","怎么","天气","很好","哈哈"]),r"D:\semantic analysis\测试//1.pkl")
util.save_nw(set(["基本","数据","文章","集合","天气","很好","哈哈"]),r"D:\semantic analysis\测试//2.pkl")
util.save_nw(set(["重复","你们","他们","怎么","天气","消除","元素"]),r"D:\semantic analysis\测试//3.pkl")
util.save_nw(set(["我们","排序","他们","转换","类型","很好","哈哈"]),r"D:\semantic analysis\测试//4.pkl")
util.save_nw(set(["危机","为何","他们","转换","不会","友情","哈哈"]),r"D:\semantic analysis\测试//5.pkl")