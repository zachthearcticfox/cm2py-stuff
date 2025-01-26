import cm2py as cm2
import pyperclip as cb
from random import randint as rni

save = cm2.Save()

blocks = []

connections = []

ores = (
    ("Stone", 0, [107,107,107,9]),
    ("Iron", 1, [253,235,255,9]),
    ("Gold", 2, [255,180,0,9]),
    ("Diamond", 3, [85,217,255,9]),
    ("Emerald", 4, [43,252,20,9]),
    ("Ruby", 5, [255,5,5,9])
)

for i in range(40000):
    match rni(1,2):
        case 1:
            blocks.append(save.addBlock(cm2.TILE, [rni(1, 75), rni(1,75), rni(1,75)], False, ores[0][2]))
            continue
        case _: ...#print('You didn\'t get: Stone')
    match rni(1,20):
        case 1:
            blocks.append(save.addBlock(cm2.TILE, [rni(1, 75), rni(1,75), rni(1,75)], False, ores[1][2]))
            continue
        case _: ...#print('You didn\'t get: Iron')
    match rni(1,50):
        case 1:
            blocks.append(save.addBlock(cm2.TILE, [rni(1, 75), rni(1,75), rni(1,75)], False, ores[2][2]))
            continue
        case _: ...#print('You didn\'t get: Gold')
    match rni(1,125):
        case 1:
            blocks.append(save.addBlock(cm2.TILE, [rni(1, 75), rni(1,75), rni(1,75)], False, ores[3][2]))
            continue
        case _: ...#print('You didn\'t get: Diamond')
    match rni(1,240):
        case 1:
            blocks.append(save.addBlock(cm2.TILE, [rni(1, 75), rni(1,75), rni(1,75)], False, ores[4][2]))
            continue
        case _: ...#print('You didn\'t get: Emerald')
    match rni(1,370):
        case 1:
            blocks.append(save.addBlock(cm2.TILE, [rni(1, 75), rni(1,75), rni(1,75)], False, ores[5][2]))
            continue
        case _: ...#print('You didn\'t get: Emerald')
    blocks.append(save.addBlock(cm2.TILE, [rni(1, 75), rni(1,75), rni(1,75)], False, ores[0][2]))

saveString = save.exportSave()
cb.copy(saveString)