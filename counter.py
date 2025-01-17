import cm2py as cm2

save = cm2.Save()

blocks = []

connections = []

bits = 512

for i in range(bits):
    blocks.append(save.addBlock(cm2.FLIPFLOP, (i,0,0)))

for i in range(bits):
    blocks.append(save.addBlock(cm2.NOR, (i,0,2)))

for i in range(bits-1):
    connections.append(save.addConnection(blocks[i], blocks[i + 1]))

for i in range(bits):
    connections.append(save.addConnection(blocks[i], blocks[i+bits]))

blocks.append(save.addBlock(cm2.NODE, (-2,0,0), True))
connections.append(save.addConnection(blocks[-1], blocks[0]))

saveString = save.exportSave()
print(saveString)