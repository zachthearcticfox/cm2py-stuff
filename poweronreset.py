import cm2py as cm2

save = cm2.Save()

blocks = []

connections = []

blocks.append(save.addBlock(cm2.TILE, (0,0,0), state=True))

blocks.append(save.addBlock(cm2.DELAY, (2,0,0)))

blocks.append(save.addBlock(cm2.FLIPFLOP, (4,0,0)))

blocks.append(save.addBlock(cm2.NOR, (6,0,0)))

connections.append(save.addConnection(blocks[0], blocks[1]))
connections.append(save.addConnection(blocks[1], blocks[2]))
connections.append(save.addConnection(blocks[2], blocks[3]))

asciisave = save.exportSave()
print(asciisave)