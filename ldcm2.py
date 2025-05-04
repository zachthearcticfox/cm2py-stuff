import cm2py as cm2

save = cm2.Save()

blocks = []
connections = []

def draw(x0,y0,x1,y1):
    dx = x1-x0
    dy = y1-y0
    if dx != 0:
        m = dy/dx
        for i in range(dx+1):
            blocks.append(save.addBlock(cm2.TILE, (x0+i,0,round(y0 + i * m))))

draw(0,0,29,16)

saveString = save.exportSave()
print(saveString)