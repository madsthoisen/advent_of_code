import re
import functools

import numpy as np


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


blueprints = {i + 1: tuple(map(int, re.findall("-?\d+", line))) for i, line in enumerate(lines)}


@functools.cache
def get_geodes(t, x):
    if t <= 0:
        return 0
    if any([_x < 0 for _x in x]):
        return 0

    m1, m2, m3, m4 = 0, 0, 0, 0
    money = np.array(x[:3])
    robots = np.array(x[3:])

    # if the max needed of a resource is generated every round, not need to store
    # also, no need to store more than what could be used in remaining time
    for i in range(3):
        r = robots[i]
        m = money[i]
        _max = maxes[i]
        if r >= _max:
            money[i] = _max
        money[i] = min(m, _max * t - r * (t - 1))

    t -= 1

    # build geode
    if (money >= p_geode).all():
        _g = tuple(money + robots - p_geode)
        _r = tuple(robots)
        return get_geodes(t, _g + _r) + t

    # build obsidian
    if (money >= p_obs).all() and maxes[2] > robots[2]:
        _g = tuple(money + robots - p_obs)
        _r = (robots[0], robots[1], robots[2] + 1)
        m1 = get_geodes(t, _g + _r)

    # build clay
    if (money >= p_clay).all() and maxes[1] > robots[1]:
        _g = tuple(money + robots - p_clay)
        _r = (robots[0], robots[1] + 1, robots[2])
        m2 = get_geodes(t, _g + _r)

    # build ore
    if (money >= p_ore).all() and maxes[0] > robots[0]:
        _g = tuple(money + robots - p_ore)
        _r = (robots[0] + 1, robots[1], robots[2])
        m3 = get_geodes(t, _g + _r)

    # no build
    _g = tuple(money + robots)
    _r = tuple(robots)
    m4 = get_geodes(t, _g + _r)

    return max(m1, m2, m3, m4)


add = 0
mult = 1
for k, blueprint in blueprints.items():
    get_geodes.cache_clear()
    b = blueprint

    p_ore = np.array([b[1], 0, 0])
    p_clay = np.array([b[2], 0, 0])
    p_obs = np.array([b[3], b[4], 0])
    p_geode = np.array([b[5], 0, b[6]])
    maxes = tuple(np.vstack([p_ore, p_clay, p_obs, p_geode]).max(axis=0))

    max_g = get_geodes(t=24, x=(0, 0, 0, 1, 0, 0))
    add += (max_g * k)

    if k <= 3:
        get_geodes.cache_clear()
        max_g = get_geodes(t=32, x=(0, 0, 0, 1, 0, 0))
        mult *= max_g
    if k == 3:
        print("part 2:", mult)

print("part 1:", add)
