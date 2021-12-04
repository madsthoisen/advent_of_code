import numpy as np


with open("input") as f:
    tmp = f.read().strip().split("\n\n")


boards = [
    np.array([np.array(list(map(int, line.split()))) for line in board.split("\n")])
    for board in tmp[1:]
]


won = set()
scores = []
for num in map(int, tmp[0].split(',')):
    for i in range(len(boards)):
        boards[i][boards[i] == num] = -1
        b = boards[i]
        if -5 in b.sum(0) or -5 in b.sum(1):
            won.add(i)
            score = sum(b[r][c] for r in range(5) for c in range(5) if b[r][c] != -1)
            scores.append(score * num)
        if len(won) == len(boards):
            break
    else:
        continue
    break

# part I
print(scores[0])

# part II
print(scores[-1])
