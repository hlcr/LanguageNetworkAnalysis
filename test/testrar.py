import os
import time

source = r'D:\work'

target_dir = r'D:\\'


target = target_dir + time.strftime('%Y%m%d%H%M%S')+'.rar'


rar_command = "winrar a {0} {1}".format(target, source)

if os.system(rar_command) ==0:
    print("成功")
else:
    print("失败")