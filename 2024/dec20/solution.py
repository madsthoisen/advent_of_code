from collections import defaultdict


with open("input") as f:
    lines = f.read().split("\n")


h, w = len(lines), len(lines[0])
start = next((r, c) for r in range(h) for c in range(w) if lines[r][c] == "S")
end = next((r, c) for r in range(h) for c in range(w) if lines[r][c] == "E")


path = [start]
r, c = start
while (r, c) != end:
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if lines[nr][nc] != "#" and (nr, nc) not in path:
            path.append((r := nr, c := nc))

shortcuts_2 = defaultdict(int)
shortcuts_20 = defaultdict(int)
for i, (r1, c1) in enumerate(path):
    for dist, (r2, c2) in enumerate(path[i:]):
        manh = abs(r1 - r2) + abs(c1 - c2)
        saved = dist - manh
        if manh <= 2:
            shortcuts_2[saved] += 1
        if manh <= 20:
            shortcuts_20[saved] += 1

# part I
print(sum(v for k, v in shortcuts_2.items() if k >= 100))

# part II
print(sum(v for k, v in shortcuts_20.items() if k >= 100))
