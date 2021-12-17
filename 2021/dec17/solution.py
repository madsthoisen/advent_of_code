import re

from itertools import count


with open("input") as f:
    min_x, max_x, min_y, max_y = list(map(int, re.findall('-?\d+', f.read())))


# Starting with a v_y > 0, the probe will always return to y-position 0
# and thus we don't need to try initial v_y's larger than the abs(min_y)
within = 0
max_height = 0
for vy_ in range(min_y, abs(min_y) + 1):
    for vx in range(max_x + 1):
        vy = vy_
        x, y = 0, 0
        M = 0
        for _ in count(1):
            x, y = x + vx, y + vy
            vx, vy = max(0, vx - 1), vy - 1
            M = max(M, y)
            if min_x <= x <= max_x and min_y <= y <= max_y:
                max_height = max(M, max_height)
                within += 1
                break
            if y < min_y or x > max_x:
                break

# part I
print(max_height)

# part II
print(within)

