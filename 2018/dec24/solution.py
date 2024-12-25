import re

from collections import defaultdict
from dataclasses import dataclass
from functools import partial


with open("test") as f:
    a, b = [b.split("\n") for b in f.read().split("\n\n")]


@dataclass
class Group:
    id: int
    n: int
    typ: str
    hit: int
    dam: int
    init: int
    weak: set
    immune: set


    @property
    def effective_power(self):
        return self.n * self.dam


def create_army(lines):
    army = {}
    for id, line in enumerate(lines):
        amnt, hit, dam, init = map(int, re.findall(r"\d+", line))
        typ = line.split(' ')[-5]
        x = re.findall(r"\((.*)\)", line)
        weak = set()
        immune = set()
        if x:
            ss = [sp.replace(',', '').split(' ') for sp in x[0].split('; ')]
            for s in ss:
                if s[0] == "weak":
                    for a in s[2:]:
                        weak.add(a)
                if s[0] == "immune":
                    for a in s[2:]:
                        immune.add(a)
        army[id + 1] = Group(n=amnt, id=id + 1, typ=typ, hit=hit, dam=dam, init=init, weak=weak, immune=immune)
    return army


def damage(attack: Group, defence: Group):
    if attack.typ in defence.immune:
        return 0
    damage = attack.effective_power
    if attack.typ in defence.weak:
        damage *= 2
    return damage


def deal_damage(defence: Group, damage: int):
    kill = damage // defence.hit
    print(f"killing {kill} units")
    defence.n -= kill


def fight(immune, infection):
    def choose(_att, _def):
        chosen = {}
        for a in sorted(_att.values(), key=lambda x: (x.effective_power, x.init), reverse=True):
            def dam(x): return damage(a, x)
            ll = sorted(list(_def.values()), key=lambda x:(dam(x), x.effective_power, x.init), reverse=True)[0]
            if dam(ll) > 0 and ll.id not in _att.values():
                chosen[a.id] = ll.id
        return chosen
    f_immune = choose(immune, infection)
    f_infection = choose(infection, immune)
    for a in list(immune.values()) + list(infection.values()):
        print(a)




immune = create_army(a[1:])
infection = create_army(b[1:])
fight(immune, infection)


