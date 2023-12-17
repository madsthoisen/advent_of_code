from heapq import heappop, heappush


with open("input") as f:
    grid = [line.strip() for line in f.readlines()]


ROWS, COLS = len(grid), len(grid[0])


def solve(min_len, max_len):
    curr = [(0, 0, 0, 1, 0), (0, 0, 0, 0, 1)]
    seen = set()
    while curr:
        score, r, c, dr, dc = heappop(curr)
        if r == ROWS - 1 and c == COLS - 1:
            return score
        if (r, c, dr, dc) in seen:
            continue
        seen.add((r, c, dr, dc))
        dirs = {(-1, 0), (1, 0)} if dr == 0 else {(0, -1), (0, 1)}
        for n in range(min_len, max_len + 1):
            for dr, dc in dirs:
                rr, cc = r + n * dr, c + n * dc
                if 0 <= rr < ROWS and 0 <= cc < COLS:
                    new_score = score + sum(int(grid[r + dr * i][c + dc * i]) for i in range(1, n + 1))
                    heappush(curr, (new_score, rr, cc, dr, dc))


# part I
print(solve(1, 3))

# part II
print(solve(4, 10))
