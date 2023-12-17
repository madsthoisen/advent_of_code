from collections import defaultdict


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


ROWS, COLS = len(lines), len(lines[0])
GOAL = (ROWS - 1, COLS - 1)
OPP = {(1, 0): (-1, 0), (-1, 0): (1, 0), (0, 1): (0, -1), (0, -1): (0, 1)}
ALL_DIRS = {(-1, 0), (1, 0), (0, -1), (0, 1)}


def solve(part2):
    min_len = 4 if part2 else 0
    max_len = 10 if part2 else 3
    curr = {((0, 0), 0, False): 0}
    seen = {((0, 0), 0, False): 0}
    winner = 999_999
    while curr:
        new_curr = defaultdict(lambda: 999_999)
        for ((r, c), count, d), score in curr.items():
            if not d:
                dirs = ALL_DIRS
            elif count < min_len:
                dirs = {d}
            elif min_len <= count < max_len:
                dirs = ALL_DIRS - {OPP[d]}
            elif count == max_len:
                dirs = ALL_DIRS - {OPP[d], d}

            for new_d in dirs:
                rr, cc = r + new_d[0], c + new_d[1]
                if not 0 <= rr < ROWS or not 0 <= cc < COLS:
                    continue

                new_count = count + 1 if new_d == d else 1
                new_pos = (rr, cc)
                new_score = score + int(lines[rr][cc])
                new_tup = (new_pos, new_count, new_d)

                if new_tup in seen and seen[new_tup] < new_score:
                    continue
                seen[new_tup] = new_score

                if new_pos == GOAL and new_count >= min_len:
                    winner = min(winner, new_score)

                new_curr[new_tup] = min(new_curr[new_tup], new_score)
        curr = new_curr
    return winner


# part I
print(solve(False))

# part II
print(solve(True))
