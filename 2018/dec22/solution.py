from collections import defaultdict
from math import inf


class State:
    def __init__(self, target, depth):
        self.x_size = 1
        self.y_size = 1
        self.depth = depth
        self.target = target
        self.index = {(0, 0): 0}
        self.erosion = {(0, 0): self.depth % 20183}
        self.cave = {(0, 0): '.'}
        self.risk = {'.': 0, '=': 1, '|': 2}
        self.types = {0: '.', 1: '=', 2: '|'}
        self.valid_tools = {'.': {'c', 't'}, '=': {'c', 'n'}, '|': {'t', 'n'}}

    def expand_cave(self, d):
        if d == 'x':
            x = self.x_size
            for y in range(self.y_size):
                if y == 0:
                    self.index[(x, y)] = x * 16807
                else:
                    self.index[(x, y)] = self.erosion[(x - 1, y)] * self.erosion[(x, y - 1)]
                if (x, y) == self.target:
                    self.index[(x, y)] = 0
                self.erosion[(x, y)] = (self.index[(x, y)] + self.depth) % 20183
                self.cave[(x, y)] = self._get_type(self.erosion[(x, y)])
            self.x_size += 1
        if d == 'y':
            y = self.y_size
            for x in range(self.x_size):
                if x == 0:
                    self.index[(x, y)] = y * 48271
                else:
                    self.index[(x, y)] = self.erosion[(x - 1, y)] * self.erosion[(x, y - 1)]
                if (x, y) == self.target:
                    self.index[(x, y)] = 0
                self.erosion[(x, y)] = (self.index[(x, y)] + self.depth) % 20183
                self.cave[(x, y)] = self._get_type(self.erosion[(x, y)])
            self.y_size += 1

    def _get_type(self, n):
        return self.types[n % 3]

    def draw_map(self):
        m = ''
        for y in range(self.y_size):
            for x in range(self.x_size):
                m += self.cave[(x, y)]
            m += '\n'
        print(m)
    
    def get(self, x, y):
        if (x, y) in self.cave:
            return self.cave[(x, y)]
        else:
            while self.x_size < x + 1:
                self.expand_cave('x')
            while self.y_size < y + 1:
                self.expand_cave('y')
            return self.cave[(x, y)]
    
    def _get_risk(self, x, y):
        return self.risk[state.get(x, y)]

    def get_total_risk(self):
        return sum(self._get_risk(x, y) for x in range(self.target[0] + 1) for y in range(self.target[1] + 1))
    
    def shortest_path_to_target(self):
        current = {(0, 0, 't'): 0}
        seen = {(0, 0, 't'): 0}
        m = 1e10
        moves = 0
        while current:
            moves += 1
            new_current = defaultdict(lambda: inf)
            for (x, y, t), time in current.items():
                other_tool = self.valid_tools[self.get(x, y)].difference({t}).pop()
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x_t, y_t = x + i, y + j
                    if x_t < 0 or y_t < 0:
                        continue

                    # keep tool and move if possible
                    if t in self.valid_tools[self.get(x_t, y_t)]:
                        c = (x_t, y_t, t)
                        new_current[c] = min(new_current[c], time + 1)

                    # change tool and move if possible
                    if other_tool in self.valid_tools[self.get(x_t, y_t)]:
                        c = (x_t, y_t, other_tool)
                        new_current[c] = min(new_current[c], time + 8)
            current = {}
            for c, time in new_current.items():
                if c in seen:
                    if time < seen[c]:
                        seen[c] = time
                        if time < m:
                            current[c] = time
                else:
                    seen[c] = time
                    if time < m:
                        current[c] = time
                if (c[0], c[1]) == self.target:
                    final_time = new_current[c] if c[2] == 't' else new_current[c] + 7
                    m = min(m, final_time)
        return m


DEPTH, TARGET = 5616, (10, 785)

state = State(TARGET, DEPTH)
print("part 1:", state.get_total_risk())
print("part 2:", state.shortest_path_to_target())
