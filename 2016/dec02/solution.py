with open("input") as f:
    instructions = f.read().strip().split('\n')


def get_key(ins, pad, pos):
    for i in ins:
        if i == 'L':
            tmp = (pos[0] - 1, pos[1])
        elif i == 'R':
            tmp = (pos[0] + 1, pos[1])
        elif i == 'U':
            tmp = (pos[0], pos[1] + 1)
        elif i == 'D':
            tmp = (pos[0], pos[1] - 1)
        if tmp in pad.keys():
            pos = tmp
    return pad[pos]


# part I
pad = {(-1, 1): 1, (0, 1): 2, (1, 1): 3,
       (-1, 0): 4, (0, 0): 5, (1, 0): 6,
       (-1, -1): 7, (0, -1): 8, (1, -1): 9}

print(''.join(str(get_key(ins, pad, (0, 0))) for ins in instructions))

# part II
pad = {(0, 2): 1, (-1, 1): 2, (0, 1): 3, (1, 1): 4, (-2, 0): 5, (-1, 0): 6,
       (0, 0): 7, (1, 0): 8, (2, 0): 9, (-1, -1): 'A', (0, -1): 'B', (1, -1):
       'C', (0, -2): 'D'}

print(''.join(str(get_key(ins, pad, (-2, 0))) for ins in instructions))
