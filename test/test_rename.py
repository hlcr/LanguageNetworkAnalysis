import util
import os

dirr = 'D:\semantic analysis\mpkl//'
# dirr = 'D:\semantic analysis\c_date\gm//'
k_list = util.get_key_list()
for kw in k_list:
    print(kw)
    srcd = dirr+kw+'//p//'
    fl = util.get_file_list(srcd, '-')
    for f in fl:
        os.rename(srcd+f, srcd+f+'.pkl')