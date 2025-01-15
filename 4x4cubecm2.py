import cm2py as cm2
import random as rn

save = cm2.Save()

blocks = []

connections = []

pos = [0,0,0]

for i in range(65):
    blocks.append(save.addBlock(cm2.TILE, tuple(pos), False, [rn.randint(0, 255), rn.randint(0, 255), rn.randint(0,255)]))
    if i % 4 == 0 and i != 0 and i % 16 != 0:
        pos[2] += 2
        pos[0] = 0
    elif i % 16 == 0 and i != 0: 
        pos[1] += 2
        pos[0], pos[2] = 0, 0
    elif i % 4 != 0 and i % 16 != 0: pos[0] += 2


asciisave = save.exportSave()
print(asciisave)