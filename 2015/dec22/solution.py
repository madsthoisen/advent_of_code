import re

with open("input") as f:
    boss = tuple(map(int, re.findall(r"\d+", f.read())))


def round(me, boss, i, action):
    armor = 7 if me[2] > 0 else 0
    if me[3] > 0:
        boss = (boss[0] - 3, boss[1])
    if me[4] > 0:
        me = (me[0], me[1] + 101, me[2], me[3], me[4])

    me = (me[0], me[1], max(me[2] - 1, 0), max(me[3] - 1, 0), max(me[4] - 1, 0))

    damage = 0
    if i == 0: # my turn
        if action == "Magic Missile":
            damage = 4
            me = (me[0], me[1] - 53, me[2], me[3], me[4])
        elif action == "Drain":
            damage = 2
            me = (me[0] + 2, me[1] - 73, me[2], me[3], me[4])
        elif action == "Shield":
            me = (me[0], me[1] - 113, me[2] + 6, me[3], me[4])
        elif action == "Poison":
            me = (me[0], me[1] - 173, me[2], me[3] + 6, me[4])
        elif action == "Recharge":
            me = (me[0], me[1] - 229, me[2], me[3], me[4] + 5)
        boss = (boss[0] - damage, boss[1]) 

    elif i == 1: # boss' turn
        me = (me[0] - max(boss[1] - armor, 1), me[1], me[2], me[3], me[4])

    return me, boss

def play(me, boss, part2=False):
    costs = set()
    stats = {(me, boss, 0)}
    r = 0
    while True:
        new_stats = set() 
        for me, boss, cost in stats:
            if part2 and r == 0:
                me = (me[0] - 1, me[1], me[2], me[3], me[4])
            for a in actions:
                cost_tmp = cost + actions[a] if r == 0 else cost
                me_tmp, boss_tmp = round(me, boss, r, a)
                if me_tmp[1] < 0:
                    continue
                if me_tmp[0] > 0:
                    new_stats.add((me_tmp, boss_tmp, cost_tmp))
                if boss_tmp[0] < 1:
                    costs.add(cost_tmp)
        r = (r + 1) % 2
        stats = new_stats.copy()
        if len(costs) > 0:
            return min(costs)

actions = {"Magic Missile": 53,
           "Drain": 73,
           "Shield": 113,
           "Poison": 173,
           "Recharge": 229}

# part I
me = (50, 500, 0, 0, 0)
print(play(me, boss))

# part I
me = (50, 500, 0, 0, 0)
print(play(me, boss, True))
