import cm2py as cm2
save, blocks, connections = cm2.Save(),[],[]

edit = 1

savetty = [ # 8x8 Grid
    [[[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]]],
    [[[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]]],
    [[[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]]],
    [[[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]]],
    [[[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]]],
    [[[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]]],
    [[[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]]],
    [[[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]], [[None, False, []]]]
]

while edit:
    command = input('type \'help\' for a list of commands. - cm2 shell > ')
    if command == 'help':
        print('add block [blockID / cm2.BlockName] [PosX] [PosZ]')
        print('list block ids')
        print('export and exit')
        print('don\'t save and exit')
    elif command == 'list block ids':
        print('NOR=1, AND=2, OR=3, XOR=4, BUTTON=5, 6=TFF, 7=LED, 8=SOUND, 9=CONDUCTOR, 11=NAND, 12=XNOR, 13=RANDOM, 14=TEXT, 15=TILE, 16=NODE, 17=DELAY, 18=ANTENNA, 19=CONDUCTOR-V2')
    elif command.startswith('add block '):
        splitted_addblock = command.split(' ')[2:]
        savetty[int(splitted_addblock[2])][int(splitted_addblock[1])][0] = int(splitted_addblock[0])
    elif command == 'don\'t save and exit': exit(f'Exit Code: {2} (Successful)')
    elif command == 'export and exit':
        for i in savetty:
            for j in i:
                if j[0] == None: continue
                blocks.append(save.addBlock(j[0], (i, 0, j), j[1]))
        asciisave = save.exportSave()
        exit(f'Exit Code: {3} (Successful)')