import re

with open("input") as f:
    lines = [line.strip()for line in f.readlines()]


def create_mapping(l_):
    l = sorted(set(l_))
    dic = {val: i for i, val in enumerate(l)}
    lengths = [l[i + 1] - l[i] for i in range(len(l) - 1)]
    return dic, lengths


x_list, y_list, z_list = [], [], []
for line in lines:
    x0, x1, y0, y1, z0, z1 = list(map(int, re.findall("-?\d+", line)))
    x_list.extend([x0, x1 + 1])
    y_list.extend([y0, y1 + 1])
    z_list.extend([z0, z1 + 1])

x_map, x_lengths = create_mapping(x_list)
y_map, y_lengths = create_mapping(y_list)
z_map, z_lengths = create_mapping(z_list)

lights = {}
for i, line in enumerate(lines):
    x0, x1, y0, y1, z0, z1 = list(map(int, re.findall("-?\d+", line)))
    print(i, len(lines))
    mode = int(line[:2] == 'on')
    for x in range(x_map[x0], x_map[x1 + 1]):
        for y in range(y_map[y0], y_map[y1 + 1]):
            for z in range(z_map[z0], z_map[z1 + 1]):
                lights[(x, y, z)] = mode

print(sum(x_lengths[x] * y_lengths[y] * z_lengths[z] for (x, y, z), v in lights.items() if v))
