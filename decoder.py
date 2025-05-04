import cm2py as cm2

save = cm2.Save()
output_andgates = []
input_nodes = []
input_ors = []
input_nors = []
connections = []
bitcount = 5
currentdec = 0
currentbin = ''.join(['0' for i in range(bitcount)])
anditer = 0
binarylist = []
binarylist.append(currentbin)

for i in range(bitcount):
    input_nodes.append(save.addBlock(cm2.NODE, (i,0,0)))
    input_ors.append(save.addBlock(cm2.OR, (i,0,1)))
    input_nors.append(save.addBlock(cm2.NOR, (i,0,2)))

for i in range(bitcount):
    connections.append(save.addConnection(input_nodes[i], input_ors[i]))
    connections.append(save.addConnection(input_nodes[i], input_nors[i]))

for i in range(2**bitcount):
    output_andgates.append(save.addBlock(cm2.AND, (5,0,i+3)))

for i in range(2**bitcount-1):
    currentdec = currentdec + 1
    currentbin = f'{currentdec:05b}'
    binarylist.append(currentbin)

for i in range(2**bitcount):
    connections.append(save.addConnection(input_ors[anditer], output_andgates[i])) if currentbin[anditer] == '1' else connections.append(save.addConnection(input_nors[anditer], output_andgates[i]))
    anditer += 1
    connections.append(save.addConnection(input_ors[anditer], output_andgates[i])) if currentbin[anditer] == '1' else connections.append(save.addConnection(input_nors[anditer], output_andgates[i]))
    anditer += 1
    connections.append(save.addConnection(input_ors[anditer], output_andgates[i])) if currentbin[anditer] == '1' else connections.append(save.addConnection(input_nors[anditer], output_andgates[i]))
    anditer += 1
    connections.append(save.addConnection(input_ors[anditer], output_andgates[i])) if currentbin[anditer] == '1' else connections.append(save.addConnection(input_nors[anditer], output_andgates[i]))
    anditer += 1
    connections.append(save.addConnection(input_ors[anditer], output_andgates[i])) if currentbin[anditer] == '1' else connections.append(save.addConnection(input_nors[anditer], output_andgates[i]))
    anditer += 1
    anditer = 0

print(binarylist)

asciisave = save.exportSave()
print(asciisave)