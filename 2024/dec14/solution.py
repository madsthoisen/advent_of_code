import numpy as np
import re

from collections import defaultdict
from itertools import count


with open("input") as f:
    lines = [tuple(map(int, re.findall(r"-?\d+", line.strip()))) for line in f.readlines()]


def move(p, v):
    return (p[0] + v[0]) % (max_x + 1), (p[1] + v[1]) % (max_y + 1)


def get_part1(robots):
    hx, hy = max_x // 2, max_y // 2
    quadrants = defaultdict(int)
    for r, vs in robots.items():
        if r[1] == hy or r[0] == hx:
            continue
        quadrants[(r[0] < hx, r[1] < hy)] += len(vs)
    return np.prod(list(quadrants.values()))


robots = defaultdict(list)
for px, py, vx, vy in lines:
    robots[(px, py)].append((vx, vy))
max_x = max(x for (x, y) in robots)
max_y = max(y for (x, y) in robots)


max_heuristic = 0
for round_no in count(1):
    new_robots = defaultdict(list)
    for robot, velocities in robots.items():
        for v in velocities:
            new_robots[move(robot, v)].append(v)
    robots = new_robots
    if round_no == 100:
        print(f"part 1: {get_part1(robots)}")

    nn = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    heuristic = sum((pr + dr, pc + dc) in robots for pr, pc in robots for dr, dc in nn)
    if heuristic > max_heuristic:
        max_heuristic = heuristic
        img = '\n'.join(''.join('#' if (x, y) in robots else '.' for x in range(max_x + 1)) for y in range(max_y + 1))
        print(f"round {round_no}\n{img}")
