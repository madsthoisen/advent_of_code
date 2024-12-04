from collections import defaultdict


with open("input") as f:
    lines = f.read().strip().split("\n")


nrows, ncols = len(lines), len(lines[0])
word = defaultdict(lambda: ".", {(r, c): lines[r][c] for r in range(nrows) for c in range(ncols)})

part1, part2 = 0, 0
for r in range(nrows):
    for c in range(ncols):
        if word[(r, c)] == "X":
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if [word[(r + i * dr, c - i * dc)] for i in range(4)] == ["X", "M", "A", "S"]:
                    part1 += 1
        if word[(r, c)] == "A":
            diag1 = word[(r-1, c-1)] + word[(r+1, c+1)]
            diag2 = word[(r-1, c+1)] + word[(r+1, c-1)]
            if diag1 in {"MS", "SM"} and diag2 in {"MS", "SM"}:
                part2 += 1

# part I
print(part1)


# part II
print(part2)
