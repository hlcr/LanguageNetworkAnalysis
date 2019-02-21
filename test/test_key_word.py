import util
import jieba


# 所有句子分句，并且生成矩阵
def get_word_list(s_list):
    # 存放所有分句分词后的结果
    ps_list = []
    for sentence in s_list:
        # 过滤并把一个句子切成分句
        spl = util.input_filer(sentence)
        for sp in spl:
            swl = jieba.cut(sp, cut_all=False)
            for ssp in swl:
                if len(ssp) > 1:
                    ps_list.append(ssp)
    return ps_list


def count_word(it, w_dict):
    for node in it:
        num = w_dict.get(node)
        if num is None:
            w_dict[node] = 1
        else:
            w_dict[node] = num+1
    return w_dict


klist = ['正能量', '完爆', '扯淡', '达人', '接地气', '纠结', '吐槽', '淡定', '自拍']

txt_dir = 'D:\semantic analysis\c_date//'
jieba.set_dictionary("D://fc\dict1.txt")
jieba.initialize()
for key in klist:
    r_dict = {}
    r_list = []
    print(key)
    # 获取文件列表
    f_list = util.get_file_list(txt_dir+key, '.txt')
    for file in f_list:
        w_list = util.get_list_from_file(txt_dir+key+'//'+file)
        rl = get_word_list(w_list)
        count_word(rl, r_dict)

    # 保存结果
    for (k, v) in r_dict.items():
        r_list.append(k + '\t' + str(v))
    util.save_file('D://fc//result//'+key+'.txt',r_list)
