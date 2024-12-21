import itertools

from collections import defaultdict


with open("input") as f:
    lines = f.read().split("\n")


DIRS = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
POS_DIR = {'A': (0, 2), '^': (0, 1), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}
POS_NUM = {"0": (3, 1), 'A': (3, 2), '1': (2, 0), '2': (2, 1), '3': (2, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (0, 0), '8': (0, 1), '9': (0, 2)}


def cost(s):
    manh = sum(sum(abs(x - y) for x, y in zip(POS_DIR[a], POS_DIR[b])) for a, b in zip(s, s[1:]))
    switch = sum(b != a for a, b in zip(s, s[1:]))
    final = [{'^': 0, '<': 1, 'v': 2, '>': 3, 'A': 4}[x] for x in s]  # magic order :)
    return manh, switch, final


def ways_to_pos(pos, newpos, nogo):
    s = abs(newpos[0] - pos[0]) * ('v' if newpos[0] > pos[0] else '^')
    s += abs(newpos[1] - pos[1]) * ('>' if newpos[1] > pos[1] else '<')
    res = []
    paths = set(itertools.permutations(s, len(s)))
    for path in paths:
        r, c = pos
        if nogo not in {(r := r + DIRS[x][0], c := c + DIRS[x][1]) for x in path}:
            res.append(''.join(path) + 'A')
    return sorted(res, key=cost)[0]


def get_shortest(iterations, ways_numeric, ways_dir):
    shortest = ways_numeric
    for i in range(iterations):
        new_shortest = {}
        for k, _ways in shortest.items():
            atomval = defaultdict(int)
            for pat, amnt in _ways.items():
                pos = (0, 2)
                for c in pat:
                    newpos = POS_DIR[c]
                    s = ways_dir[pos, newpos]
                    pos = newpos
                    atomval[s] += amnt
            new_shortest[k] = atomval
        shortest = new_shortest
    return shortest


def run(code, shortest):
    pos = (3, 2)
    ans = 0
    for c in code:
        newpos = POS_NUM[c]
        ans += sum(len(k) * v for k, v in shortest[pos, newpos].items())
        pos = newpos
    return ans

positions = [(r, c) for r in range(4) for c in range(3) if (r, c) != (3, 0)]
ways_numeric = {(pos, newpos): {ways_to_pos(pos, newpos, (3, 0)): 1} for pos in positions for newpos in positions}

positions = [(r, c) for r in range(2) for c in range(3) if (r, c) != (0, 0)]
ways_directional = {(pos, newpos): ways_to_pos(pos, newpos, (0, 0)) for pos in positions for newpos in positions}

# part I
shortest = get_shortest(iterations=2, ways_numeric=ways_numeric, ways_dir=ways_directional)
print(sum(run(code, shortest) * int(code[:3]) for code in lines))


# part II
shortest = get_shortest(iterations=25, ways_numeric=ways_numeric, ways_dir=ways_directional)
print(sum(run(code, shortest) * int(code[:3]) for code in lines))
