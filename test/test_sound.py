import tool.util as util

dirr = 'C://Users//user\Desktop\听力会//n2.txt'

wl = util.get_list_from_file(dirr)
sentence = ''
i = 0
for word in wl:
    sentence = sentence + word + ', '
    sentence = sentence + word + ', '
    sentence = sentence + word + ', '
    sentence = sentence + word + '. '
    sentence = sentence + '\n'


print( sentence)