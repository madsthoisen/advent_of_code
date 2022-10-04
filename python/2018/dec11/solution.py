import numpy as np


def power(x, y):
    serial_number = 6878
    return (((x + 10) * y + serial_number) * (x + 10)) // 100 % 10 - 5


grid = np.matrix([[power(x, y) for x in range(1, 301)] for y in range(1, 301)])
m = 0
for size in range(3, 301):
    for x in range(300 - size):
        for y in range(300 - size):
            if (tmp := grid[y : y + size, x : x + size].sum()) > m:
                m = tmp
                loc = (x + 1, y + 1, size)
    if size == 3:
        print(f"part I: {loc[0], loc[1]}")
print(f"part II: {loc}")
