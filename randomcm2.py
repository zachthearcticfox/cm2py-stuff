import cm2py as cm2
import random as rng

save = cm2.Save()

blocks = []

connections = []

for i in range(2000):
    if rng.randint(1, 2) == 1:
        blocks.append(save.addBlock(cm2.LED, (rng.randint(0,100), rng.randint(0,100), rng.randint(0,100)), properties=[rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255), 100, rng.randint(5, 100)]))
    else:
        blocks.append(save.addBlock(cm2.TEXT, (rng.randint(0,100), rng.randint(0,100), rng.randint(0,100)), properties=[rng.randint(0, 127)]))

saveString = save.exportSave()
print(saveString)