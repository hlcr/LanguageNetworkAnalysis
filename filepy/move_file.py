# 把一个目录下的所有文件移动到另一个目录下，作为镜像
import shutil
import tool.util as util
import os

keyword_list = util.get_key_list2()

parent_dir = "D:\semantic analysis\新结果\去虚词去单字\共现网络\{0}\p\\"


for key in keyword_list:
    k_dir = parent_dir.format(key)
    file_list = util.get_file_list(k_dir, ".pkl")
    util.create_directory(k_dir + "e")
    for file in file_list:
        if "2009" in file or "2010-01" in file or "2010-02" in file or "2010-03" in file or "2010-04" in file:
            shutil.move(k_dir + file, k_dir + "e//" + file)



# os.chdir(xls_parent)
# word_list = util.get_key_list()
# for word in word_list:
#     util.create_directory(dst_dir + word)
#     shutil.move(xls_parent + word + '//w//',dst_dir + word)

#
# xml_files_list = os.listdir("./")
#
# for xml_file in xml_files_list:
#     xml_list = util.get_file_list(xls_parent+xml_file,'xml')
#     for xml in xml_list:
#         util.create_directory(dst_dir+xml_file)
#         shutil.move(xls_parent+xml_file+'//'+xml, dst_dir+xml_file+'//'+xml)


