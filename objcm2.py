import cm2py as cm2
from pyperclip import copy as cbcpy

save = cm2.Save()
blocks = []
connections = []

fnm = input('Enter File path: ')
plusyoff = int(input('+Y Offset: '))

with open(fnm, 'rt') as objf:
    f = objf.read()
    lines = f.splitlines()
    for l in lines:
        if l.startswith('v  '):
            splitl = l.split('v  ')[1].split(' ')
            for i in range(len(splitl)):
                try:
                    splitl[i] = float(splitl[i])
                except ValueError as e:
                    splitl[i] = 0.0
                
            try:
                splitl[1], splitl[2] = splitl[2], splitl[1]
                splitl[1] = splitl[1] + plusyoff
                blocks.append(save.addBlock(cm2.TILE, tuple(splitl), False, [255,255,255, 2], snapToGrid=False))
            except AssertionError as e:
                blocks.append(save.addBlock(cm2.TILE, (0,0,0), snapToGrid=True))

ascsave = save.exportSave()
print(ascsave)

cbcpy(ascsave)