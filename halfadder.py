# This file is really just used to copy paste into new files

import cm2py as cm2

save = cm2.Save()

blocks = []

connections = []

blocks.append(save.addBlock(cm2.FLIPFLOP, (0,0,0)))
blocks.append(save.addBlock(cm2.FLIPFLOP, (2,0,0)))

blocks.append(save.addBlock(cm2.AND, (0,0,2)))
blocks.append(save.addBlock(cm2.XOR, (2,0,2)))

connections.append(save.addConnection(blocks[0], blocks[2]))
connections.append(save.addConnection(blocks[1], blocks[3]))
connections.append(save.addConnection(blocks[0], blocks[3]))
connections.append(save.addConnection(blocks[1], blocks[2]))

blocks.append(save.addBlock(cm2.LED, (0,0,4)))
blocks.append(save.addBlock(cm2.LED, (2,0,4)))

connections.append(save.addConnection(blocks[2], blocks[4]))
connections.append(save.addConnection(blocks[3], blocks[5]))

asciisave = save.exportSave()
print(saveString)