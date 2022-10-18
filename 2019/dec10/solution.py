from itertools import count
from math import atan, pi
from sympy import gcd


with open("input") as f:
    space = [line.strip() for line in f.readlines()]


def angle(x, y):
    # angle with y-axis
    if x != 0:
        v = pi / 2 - atan(-y / x)
        if x < 0:
            return v + pi
    else:
        return 0 if y < 0 else pi
    return v


def kill(asteroids, dirs):
    n_dead = 0
    while True:
        for x_s, y_s in dirs:
            for i in count(1):
                if (tmp := (x + x_s * i, y + y_s * i)) in asteroids:
                    n_dead += 1
                    asteroids.remove(tmp)
                    if n_dead == 200:
                        return(tmp[0]*100 + tmp[1])
                    break
                elif tmp[0] < 0 or tmp[0] > w or tmp[1] < 0 or tmp[1] > h:
                    break


w, h = len(space[0]), len(space)
asteroids = {(x, y) for y in range(h) for x in range(w) if space[y][x] == '#'}

# part I
visible = {a: {angle(x - a[0], y - a[1]) for x, y in asteroids - {a}} for a in asteroids}
(x, y), vis = max(visible.items(), key=lambda x: len(x[1]))
print("part 1:", len(vis))

# part II
incs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
slopes = [(n*a, d*b) for n in range(h) for d in range(w) for a, b in incs if gcd(n, d) == 1]
dirs = sorted(set(slopes),key=lambda x: angle(x[0], x[1]))
print("part 2:", kill(asteroids, dirs))

