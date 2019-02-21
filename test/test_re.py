import re
import os

local_dir = r"H:\新浪微博_搜索列表狗带\新浪微博_搜索列表狗带//"
file = "新浪微博_搜索列表狗带_210445254_4058327584.xml"
with open(local_dir + file, "rb") as f:
    row1 = f.readline().decode("utf-8")
    # 记录只有一页的页面
    if r"<pageno>0</pageno>" in row1:
        url = re.search(r"<fullpath><!\[CDATA\[(\S+)\]\]></fullpath>", row1).group(1)
        print(url)
        with open(local_dir + "one_page_record.txt", "a") as f1:
            f1.write(url+"\n")
