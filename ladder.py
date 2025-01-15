import cm2py as cm2
import pyperclip as cb

save = cm2.Save()

blocks = []

connections = []

height = 10
ylev = 0

for i in range(height):
    blocks.append(save.addBlock(cm2.TILE, (0, ylev, 0)))
    blocks.append(save.addBlock(cm2.TILE, (1, ylev, 0)))
    blocks.append(save.addBlock(cm2.TILE, (2, ylev, 0)))
    blocks.append(save.addBlock(cm2.TILE, (3, ylev, 0)))
    ylev += 2

saveString = save.exportSave()
print(saveString)
cb.copy(saveString)