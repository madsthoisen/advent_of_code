import numpy as np


with open("test") as f:
    ss = f.read()

shapes = [np.array([[1, 1, 1, 1]]),
          np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
          np.array([[0, 0, 1], [0, 0, 1], [1, 1, 1]]),
          np.array([[1], [1], [1], [1]]),
          np.array([[1, 1], [1, 1]])]

max_y = 0
i = 0
round = -1
maxes = [0 for _ in range(7)]
count = 0
while True:
    round += 1
    max_y = max(maxes)
    shape = shapes[round % 5]
    count += 1

    left = 2
    right = 2 + len(shape[0]) - 1
    vert = max_y + 3 + 1

    print()
    print("ROUND", round)
    print(maxes)
    print(shape)

    while True:
        s = ss[i]
        i += 1
        i %= len(ss)

        shape_height = len(shape)
        if s == '<' and left > 0:
            if all(maxes[left - 1] < vert + i for i in range(shape_height) if shape[-(i + 1)][0] == 1):
                left -= 1
                right -= 1
        elif s == '>' and right < 6:
            if all(maxes[right + 1] < vert + i for i in range(shape_height) if shape[-(i + 1)][-1] == 1):
                left += 1
                right += 1

        stopped = False
        for v in range(1, shape_height + 1):
            shape_row = shape[-v]
            if not stopped:
                for j in range(len(shape[0])):
                    if shape_row[j] == 1 and maxes[left + j] == vert- 1:
                        stopped = True
                        break
                    elif shape_row[j] == 1 and vert == 1:
                        stopped = True
                        break
            if stopped:
                for j in range(len(shape[0])):
                    if shape_row[j] == 1:
                        maxes[left + j] = vert + v - 1
        vert -= 1

        if stopped:
            break

    print("MAXES", maxes)
    if count == 2022:
        break

# 3148 too low