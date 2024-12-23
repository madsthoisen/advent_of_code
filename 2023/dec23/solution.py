from collections import defaultdict
from heapq import heappop, heappush


with open("input") as f:
    grid = f.read().split("\n")


DIRS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

h, w = len(grid), len(grid[0])
grid = defaultdict(lambda: "#", {(r, c): grid[r][c] for r in range(h) for c in range(w)})
free = {p for p, val in grid.items() if val != "#"}
start = next((0, c) for c in range(w) if grid[0, c] == '.')
end = next((h - 1, c) for c in range(w) if grid[h - 1, c] == '.')
critical_points = {start, end} | {(r, c) for r, c in free if sum((r + dr, c + dc) in free for dr, dc in DIRS.values()) > 2}


def get_distances(icey):
    distances = defaultdict(list)
    for root in critical_points:
        bfs, seen = [root], {root}
        i = 0
        while bfs:
            i += 1
            new_bfs = []
            for r, c in bfs:
                val = grid[r, c]
                for dr, dc in DIRS.values():
                    if icey and val in DIRS and (dr, dc) != DIRS[val]:
                        continue
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in free and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        if (nr, nc) in critical_points:
                            distances[root].append(((nr, nc), i))
                        else:
                            new_bfs.append((nr, nc))
            bfs = new_bfs
    return distances


def get_longest(distances):
    dfs = [(0, start, {start})]
    maxlen = 0
    while dfs:
        nsteps, (r, c), seen = heappop(dfs)
        if (r, c) == end:
            if -nsteps > maxlen:
                maxlen = -nsteps
                print(maxlen)
            continue
        for b, ll in distances[(r, c)]:
            if b not in seen:
                heappush(dfs, (nsteps - ll, b, seen | {b}))


print("part I")
get_longest(get_distances(True))

print("part II")
get_longest(get_distances(False))
