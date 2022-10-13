from collections import defaultdict
import numpy as np


with open("input") as f:
    lines = [np.array(list(map(int, line.strip()))) for line in f.readlines()]


new_lines = []
for line in lines:
    tmp = list(line)
    tmp_line = line
    for _ in range(4):
        tmp_line = (np.array(tmp_line) + 1) % 10
        tmp_line = [x if x != 0 else 1 for x in tmp_line]
        tmp.extend(tmp_line)
    new_lines.append(np.array(tmp))
new_lines = np.array(new_lines)


tmp_line = np.array(new_lines)
new_lines = list(new_lines)
for i in range(1, 5):
    tmp_line = (tmp_line + 1) % 10
    tmp_line[tmp_line == 0] = 1
    for line in tmp_line:
        new_lines.append(line)
lines = new_lines
h, w = len(lines), len(lines[0])
stack = [((0, 0), 0)]
visited = defaultdict(lambda: 99999)
min_weight = 99999

LRUD = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(h, w)
while stack:
    new_stack = []
    while stack:
        pos, weight = stack.pop()
        for x, y in LRUD:
            p = (pos[0] + x, pos[1] + y)
            if not (0 <= p[0] < h and 0 <= p[1] < w):
                continue
            new_weight = weight + lines[p[1]][p[0]]
            if new_weight < visited[p]:
                new_stack.append((p, new_weight))
                visited[p] = new_weight
            if p == (h - 1, w - 1):
                min_weight = min(min_weight, new_weight)
    stack = new_stack

print(min_weight)

