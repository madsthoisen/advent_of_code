from collections import defaultdict
from typing import List, Dict, Tuple


with open("input") as f:
    cave = [line.strip() for line in f.readlines()]
    for line in cave:
        print(line)


class Unit:
    def __init__(self, typ: str, x: int, y: int):
        self.typ = typ
        self.attack = 3
        self.hit = 200
        self.x = x
        self.y = y

    def __gt__(self, other):
        return (self.y, self.x) >= (other.y, other.x)

    def __str__(self):
        return f"{self.typ} on {(self.x, self.y)} with attack: {self.attack} and hit: {self.hit}"

    def _is_in_range(self, units):
        for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (p := (self.x + i, self.y + j)) in units:
                if units[p].typ != self.typ:
                    return True
        return False

    def _is_pos_in_range(self, x, y, units):
        for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (p := (x + i, y + j)) in units:
                if units[p].typ != self.typ:
                    return True
        return False

    def _get_reachables(self, units, walls):
        reachables = {}
        paths = [[(self.x, self.y)]]
        while True:
            new_paths = []
            for path in paths:
                for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    p = (path[-1][0] + i, path[-1][1] + j)
                    if p in walls or p in units:
                        continue
                    if self._is_pos_in_range(p[0], p[1], units):
                        reachables[p] = path + [p]
                    else:
                        if p not in path:
                            new_paths.append(path + [p])
            paths = list(new_paths)
            if reachables:
                return reachables

class Cave:
    def __init__(self, walls: set, units: Dict[Tuple[int, int], Unit]):
        self.walls = walls
        self.units = units

w, h = len(cave[0]), len(cave)
walls = set()
units = {}
for y in range(h):
    for x in range(w):
        el = cave[y][x]
        if el == '#':
            walls.add((x, y))
        if el in {'E', 'G'}:
            units[(x, y)] = Unit(el, x, y)

cave = Cave(walls=walls, units=units)
for pos, unit in cave.units.items():
    print(pos, unit)
    print(unit._get_reachables(cave.units, cave.walls))
    break

