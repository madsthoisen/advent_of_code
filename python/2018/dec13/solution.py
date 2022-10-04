from copy import deepcopy


with open("input") as f:
    lines = [list(line) for line in f.readlines()]


h = len(lines)
carts = {}
for y in range(h):
    for x in range(len(lines[y])):
        l = lines[y][x]
        if l in {'<', '>'}:
            lines[y][x] = '-'
            carts[(y, x)] = (l, 'l')
        if l in {'v', '^'}:
            lines[y][x] = '|'
            carts[(y, x)] = (l, 'l')


def get_pos(typ, y, x):
    dic = {'<': (y, x - 1), '>': (y, x + 1), 'v': (y + 1, x), '^': (y - 1, x)}
    return dic[typ]


change_dir = {'<': {'-': '<', '\\': '^', '/': 'v'},
              '>': {'-': '>', '\\': 'v', '/': '^'},
              '^': {'|': '^', '\\': '<', '/': '>'},
              'v': {'|': 'v', '\\': '>', '/': '<'}}

plus_dir = {'<': {'l': 'v', 's': '<', 'r': '^'},
            '>': {'l': '^', 's': '>', 'r': 'v'},
            '^': {'l': '<', 's': '^', 'r': '>'},
            'v': {'l': '>', 's': 'v', 'r': '<'}}

move_dir = {'l': 's', 's': 'r', 'r': 'l'}


part_1 = False
while True:
    new_carts = {}
    removed = set()
    for (y, x) in sorted(carts.keys()):
        if (y, x) in removed:
            continue
        typ, move = carts[(y, x)]
        p = get_pos(typ, y, x)
        grid = lines[p[0]][p[1]]
        if grid == '+':
            new_val = (plus_dir[typ][move], move_dir[move])
        else:
            new_val = (change_dir[typ][grid], move)
        if p in carts or p in new_carts or p in removed:
            if not part_1:
                # part I
                print(p[::-1])
                part_1 = True
            removed.add(p)
            if p in new_carts:
                del new_carts[p]
        else:
            new_carts[p] = new_val
    if len(carts) == 1:
        # part II
        print(list(carts.keys())[0][::-1])
        break
    carts = new_carts
