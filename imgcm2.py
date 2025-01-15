import cm2py as cm2
from PIL import Image
import pyperclip as cb

imgname = input('Image Name: ')
imgresx = input('Resolution (X): ')
imgresy = input('Resolution (Y): ')

img = Image.open(imgname)

def getPixels():
    global img
    img = img.resize((int(imgresx),int(imgresy)))
    w, h = img.size
    pix = list(img.getdata())
    return [pix[n:n+w] for n in range(0, w*h, w)]

img = img.transpose(Image.FLIP_LEFT_RIGHT)

pixels = list(getPixels())

save = cm2.Save()

blocks = []
connections = []

ic = int(imgresy) - 1
jc = 0

for i in getPixels():
    for j in i:
        blocks.append(save.addBlock(cm2.TILE, (jc,0,ic), properties=[j[0], j[1], j[2]]))
        jc += 1
    ic -= 1
    jc = 0

saveString = save.exportSave()
print('Copied save to clipboard')       
cb.copy(saveString)

_=input('Show Image in default image editor? (Y/n)')
if _ != 'n':
    img.show()