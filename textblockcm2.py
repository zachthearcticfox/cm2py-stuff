import cm2py as cm2

save = cm2.Save()

blocks = []
connections = []

text = input('|> ')

textascii = [ord(i) for i in text]

print(textascii)

count = 0
for i in textascii:
    blocks.append(save.addBlock(cm2.TEXT, (count,0,0), False, [i]))
    count += 1

saveString = save.exportSave()
print(saveString)