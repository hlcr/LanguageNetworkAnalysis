import random

path = r'D:\semantic analysis\采集路线\2016-10-30采集//'
with open(path+'address.txt','r') as file:
    lines = file.readlines()
    lg = len(lines)
    index = lg - 1
    while index > 0:
        i = random.randint(0,lg-1)
        lines[i],lines[index] = lines[index],lines[i]
        print(i,'<->',index)
        index = index - 1

with open(path+'cdata2.txt','w') as cfile:
    for item in lines:
        cfile.write(item)
