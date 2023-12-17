from heapq import heappop, heappush
from collections import defaultdict


with open("input") as f:
    grid = [line.strip() for line in f.readlines()]


ROWS, COLS = len(grid), len(grid[0])


def solve(min_len, max_len):
    curr = [(0, 0, 0, 1, 0), (0, 0, 0, 0, 1)]
    seen = defaultdict(lambda: 999_999)
    while curr:
        score, r, c, dr, dc = heappop(curr)
        if r == ROWS - 1 and c == COLS - 1:
            return score
        dirs = {(-1, 0), (1, 0)} if dr == 0 else {(0, -1), (0, 1)}
        for n in range(min_len, max_len + 1):
            for dr, dc in dirs:
                rr, cc = r + n * dr, c + n * dc
                if not 0 <= rr < ROWS or not 0 <= cc < COLS:
                    continue

                new_score = score + sum(int(grid[r + dr * i][c + dc * i]) for i in range(1, n + 1))
                new_tup = (rr, cc, dr, dc)

                if seen[new_tup] <= new_score:
                    continue
                seen[new_tup] = new_score
                heappush(curr, (new_score,) + new_tup)


# part I
print(solve(1, 3))

# part II
print(solve(4, 10))
