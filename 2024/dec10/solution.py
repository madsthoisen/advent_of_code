with open("input") as f:
    grid = f.read().split("\n")


h, w = len(grid), len(grid[0])
part1, part2 = 0, 0
for r in range(h):
    for c in range(w):
        val = int(grid[r][c])
        if val == 0:
            todo = {(((r, c),), val)}
            for _ in range(9):
                new_todo = set()
                for path, val in todo:
                    _r, _c = path[-1]
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = _r + dr, _c + dc
                        if 0 <= nr < h and 0 <= nc < w:
                            nval = int(grid[nr][nc])
                            if nval - val == 1:
                                new_todo.add((path + ((nr, nc),), nval))
                todo = new_todo
            part1 += len({path[-1] for path, _ in todo})
            part2 += len(todo)

# part I
print(part1)

# part II
print(part2)
