from PIL import Image
import pytesseract

# load a color image
im = Image.open('2A5C.png')


# convert to grey level image
Lim = im.convert('L')
# Lim.save('fun_Level.jpg')

# setup a converting table with constant threshold
high_threshold = 70
low_threshold = 10
table = []
for i in range(256):
    if i < low_threshold:
        table.append(1)
    elif i > high_threshold:
        table.append(1)
    else:
        table.append(0)


# convert to binary image by the table
bim = Lim.point(table, '1')
bim.show()
# bim.save('fun_binary.jpg')
import os
os.chdir("C:\Program Files (x86)\Tesseract-OCR")
vcode = pytesseract.image_to_string(im)
print(vcode)
