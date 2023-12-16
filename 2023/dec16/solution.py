from collections import defaultdict


with open("input") as f:
    lines = [line.strip() for line in f.readlines() if line != "\n"]


def solve(starting):
    mm = 0
    for curr in starting:
        energized, seen = set(), set()
        n_energized = []
        while True:
            new_curr = set()
            for pos, d in curr:
                if not 0 <= -pos.imag < rows or not 0 <= pos.real < cols:
                    continue
                if (pos, d) in seen:
                    continue
                energized.add(pos)
                seen.add((pos, d))
                x = grid[pos]
                if x == ".":
                    new_curr.add((pos + d, d))
                elif x == "/":
                    d *= 1j if d.imag == 0 else -1j
                    new_curr.add((pos + d, d))
                elif x == "\\":
                    d *= -1j if d.imag == 0 else 1j
                    new_curr.add((pos + d, d))
                if x == "|":
                    if d.real == 0:
                        new_curr.add((pos + d, d))
                    else:
                        new_curr.add((pos + d * 1j, d * 1j))
                        new_curr.add((pos + d * -1j, d * -1j))
                if x == "-":
                    if d.imag == 0:
                        new_curr.add((pos + d, d))
                    else:
                        new_curr.add((pos + d * 1j, d * 1j))
                        new_curr.add((pos + d * -1j, d * -1j))
            curr = new_curr
            n_energized.append(len(energized))
            if len(n_energized) > 3 and n_energized[-1] == n_energized[-2] == n_energized[-3]:
                mm = max(mm, len(energized))
                break
    return mm


rows, cols = len(lines), len(lines[0])
grid = defaultdict(
    lambda: ".", {c - r * 1j: lines[r][c] for r in range(rows) for c in range(cols)}
)

# part I
start = [{(0, 1)}]
print(solve(start))

# part II
start = [
    s for r in range(rows) for s in ({(-1j * r, 1)}, {(cols - 1 - 1j * r, -1)})
] + [s for c in range(cols) for s in ({(c, -1j)}, {(c - 1j * (rows - 1), 1j)})]
print(solve(start))
