# 提取分句
import os
import tool.util as util


# 判断目录是否存在后建立目录
def mk_dir(s_dir):
    if not os.path.exists(s_dir):
        os.mkdir(s_dir)


# 判断集合中的元素是否存在于分句当中
def judge_word_exist(new_set,p_sentence):
    for word in new_set:
        if word in p_sentence:
            return True
    return False


# 所有句子分句，并且生成矩阵
def extract_sentence(s_list, keyword, new_set=None,):
    # 存放所有分句分词后的结果
    ps_list = []
    pps_list = []
    for sentence in s_list:
        # 过滤并把一个句子切成分句
        spl = util.input_filer(sentence)
        for sp in spl:
            # print(sp)
            # 关键词所在的分句获取
            if keyword in sp:
                # 判断是否存在新词
                # if judge_word_exist(new_set,sp):
                    # 打印分句
                    # print(sp)
                    pps_list.append(sp)
                    ps_list.append(sentence)
    return ps_list, pps_list


def main():
    # 设置结果保存的目录
    result_dir = r'D:\semantic analysis\新纯文本\1新词分句//'
    txt_dir = r"D:\semantic analysis\新纯文本\1新词//"

    k_list = util.get_key_list()

    for key in k_list:
        print(key)
        # 文件目录
        file_list = util.get_file_list(txt_dir + key, ".txt")

        # 建立目录
        # mk_dir(result_dir+"新词整句//"+key)
        mk_dir(result_dir+key)

        for file in file_list:
            s_list = util.get_list_from_file(txt_dir + key + "//" + file)
            # 过滤相同的语句，防止重复计算
            # s_list = list(set(s_list))
            w_list, p_list = extract_sentence(s_list, key)
            util.save_file(result_dir+key+"//"+file, p_list, True)


main()