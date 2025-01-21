import cm2py as cm2

save = cm2.Save()

blocks = []
connections = []

text = input('|> ')

textascii = [ord(i) for i in text]

print(textascii)

isy = [False,False]

countx = 0
county = 0
for i in textascii:
    if isy[0] == False and i == 92:
        isy[0] = True
        continue
    elif isy[0] == True and isy[1] == False and i == 110:
        isy[1] = True
        isy = [False,False]
        countx = 0
        county += 1
        continue
    blocks.append(save.addBlock(cm2.TEXT, (countx,0,county), False, [i]))
    countx += 1

saveString = save.exportSave()
print(saveString)