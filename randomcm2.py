import cm2py as cm2
import random as rng

save = cm2.Save()

blocks = []

connections = []

for i in range(2000):
    blocks.append(save.addBlock(cm2.TEXT, (rng.randint(0,100), rng.randint(0,100), rng.randint(0,100)), properties=[rng.randint(0, 127)]))

saveString = save.exportSave()
print(saveString)