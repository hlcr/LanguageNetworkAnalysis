import tool.util as util


def remark(s_list, word_set, keyword):
    r_list = list()
    r_list.append(r"<html>")
    r_list.append("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")
    r_list.append(r"<body>")


    # 句子的处理
    for sentence in s_list:
        # 关键词的标记
        if keyword:
            sentence = sentence.replace(keyword, "<font color=\"#000FF\">" + keyword + "</font>")
        # 目标词的标记
        for word in word_set:
            sentence = sentence.replace(word, "<font color=\"#FF000\">*"+word+"</font>")
        sentence = "<p>"+sentence+"</p>"
        r_list.append(sentence)

    r_list.append(r"</body>")
    r_list.append(r"</html>")
    return r_list


def main():
    # 设置结果保存的目录
    result_dir = r'D:\semantic analysis\2016-10-05结果\html标记分句2//'
    txt_dir = r"D:\semantic analysis\2016-10-05结果\新词分句//"
    set_dir = r"D:\semantic analysis\2016-10-05结果\新词//"

    k_list = util.get_key_list()

    for key in k_list:
        print(key)
        # 文件目录
        file_list = sorted(util.get_file_list(txt_dir + key, ".txt"))
        # 集合目录
        set_list = sorted(util.get_file_list(set_dir + key, ".pkl"))

        util.create_directory(result_dir+"新词//"+key+"//")

        i = 0
        while i < len(file_list):
            s_list = util.get_list_from_file(txt_dir + key + "//" + set_list[i][0:-4]+".txt")
            new_word_list = util.get_nw(set_dir + key + "//" + set_list[i])
            # 过滤相同的语句，防止重复计算
            s_list = list(set(s_list))
            w_list = remark(s_list, new_word_list, key)
            html_name = file_list[i][:-4] + '.html'
            util.save_file(result_dir+"新词//"+key+"//"+html_name, w_list)
            i += 1

# date_list: 分段时间
# pkl_dir: pkl的路径
# 除了第一个是按照时间来，其他平分
def cal_index2(date, pkl_dir):
    r_list = []
    f_list = util.get_file_list(pkl_dir, '.txt')
    import os
    os.chdir(pkl_dir)
    # 升序排序
    set_list = sorted(f_list)

    date2 = set_list[0][0:-4]
    i = 0
    date1 = date
    # 查找出分割点所在的序号
    while i < len(set_list) and util.compare_date(date1, date2) > 0.0:
        date2 = set_list[i][0:-4]
        i += 1
    r_list.append(i)

    j = 0
    part = 2
    part_num = (len(f_list) - i) // part
    while j < part-1:
        j += 1
        r_list.append(i + j * part_num)

    r_list.append(len(f_list))
    return r_list


def main1():
    # date_list = ["2012-08-05","2011-04-05","2011-03-28","2011-10-20","2012-12-30","2011-07-30","2011-06-09","2012-02-05","2012-12-16","2011-08-01","2011-05-19","2013-09-01","2012-08-01","2013-12-01"]
    # key_list = ["吐槽","纠结","淡定","自拍","正能量","山寨","达人","腹黑","接地气","扯淡","闷骚","不明觉厉","完爆","人艰不拆"]
    date_list = ["2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31","2013-12-31"]
    key_list = ['努力', '感觉', '简单', '无聊', '希望', '美好', '气质', '害怕',  '喜欢', '不约而同', '喜闻乐见', ]

    # 设置结果保存的目录
    result_dir = r'D:\semantic analysis\2016-10-09结果\html标记结果//'
    txt_dir = r"D:\semantic analysis\纯文本\常用词分句//"
    set_dir = r"D:\semantic analysis\2016-10-09结果\中间结果//"

    i = 0

    while i < len(key_list):
        key = key_list[i]
        print(key)
        # 文件目录
        file_list = sorted(util.get_file_list(txt_dir + key, ".txt"))
        # 集合目录
        set_dir_list = util.get_file_list(set_dir + key, ".pkl")
        set_list = []
        for set_list_dir in set_dir_list:
            set_list.append(util.get_nw(set_dir + key+"//"+set_list_dir))
            print(set_list_dir)

        util.create_directory(result_dir+key+"//")
        rr = cal_index2(date_list[i], txt_dir+key_list[i])
        j = 0
        # 每个分段
        while j < len(rr):
            k = 0
            while k < rr[j]:
                print(file_list[k][:-4])
                print(rr[j])
                txt_list = util.get_list_from_file(txt_dir + key+"//"+file_list[k])
                w_list = remark(txt_list, set_list[j], key)
                html_name = file_list[k][:-4] + '.html'
                util.save_file(result_dir + key + "//" + html_name, w_list)
                k += 1
            j += 1
        i += 1


# 对关键词进行标注
def main2():
    fir = "D:\semantic analysis\整理文本\正能量//"
    xml_list = util.get_file_list(fir,"txt")
    for xml in xml_list:
        w_list = set(util.get_list_from_file(fir+xml))
        r_list = remark(w_list,(['正能量']),None)
        html_name = xml[:-4] + '.html'
        util.save_file(fir + html_name, r_list)

main2()