from dataclasses import dataclass
from itertools import count


@dataclass
class Unit:
    hit: int = 200

    def is_dead(self):
        return self.hit <= 0


@dataclass
class Goblin(Unit):
    attack: int = 3


@dataclass
class Elf(Unit):
    attack: int = 3


class Cave:
    def __init__(self, raw_cave, elf_attack):
        self.squares = {}
        for y, l in enumerate(raw_cave):
            for x, val in enumerate(l):
                if val == 'G':
                    self.squares[(x, y)] = Goblin()
                elif val == 'E':
                    self.squares[(x, y)] = Elf(attack=elf_attack)
                else:
                    self.squares[(x, y)] = val
        self.h = len(raw_cave)
        self.w = len(raw_cave[0])

    def __str__(self):
        def square_chr(sq):
            if isinstance(sq, Goblin):
                return 'G'
            if isinstance(sq, Elf):
                return 'E'
            return sq
        return '\n'.join(''.join(square_chr(self.squares[(x, y)]) for x in range(self.w)) for y in range(self.h))

    def _is_finished(self):
        def all_dead(typ):
            return all(unit.is_dead() for unit in self.squares.values() if isinstance(unit, typ))
        return all_dead(Goblin)  or all_dead(Elf)

    def n_units(self, typ):
        return sum(1 for unit in self.squares.values() if isinstance(unit, typ))

    def _get_total_hit(self):
        return sum(unit.hit for unit in self.squares.values() if isinstance(unit, Unit))

    def _get_move_order(self):
        units = [(p, unit) for p, unit in self.squares.items() if isinstance(unit, Unit)]
        return sorted(units, key=lambda x: (x[0][1], x[0][0]))

    def _get_move(self, pos, unit):
        paths = [[pos]]
        target = Goblin if isinstance(unit, Elf) else Elf
        nodes_seen = set()
        paths_seen = set()

        for l in count(0):
            good_paths = []
            new_paths = []
            new_nodes_seen = set()
            for path in paths:
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    p = (path[-1][0] + i, path[-1][1] + j)
                    if p in nodes_seen:
                        continue
                    new_nodes_seen.add(p)
                    if len(path) > 1:
                        if (path[1], p) in paths_seen:
                            continue
                        paths_seen.add((path[1], p))
                    sq = self.squares[p]
                    if isinstance(sq, target):
                        good_paths.append(path)
                    elif sq == '.':
                        new_paths.append(path + [p])
            if good_paths:
                if not l:
                    return pos
                good_paths.sort(key=lambda x: (x[-1][1], x[-1][0], x[1][1], x[1][0]))
                return good_paths[0][1]
            paths = new_paths[:]
            nodes_seen = nodes_seen.union(new_nodes_seen)
            if not paths:
                return pos

    def _move(self, unit, old_pos, new_pos):
        self.squares[new_pos] = unit
        if new_pos != old_pos:
            self.squares[old_pos] = '.'

    def _attack(self, unit, pos):
        target = Goblin if isinstance(unit, Elf) else Elf
        enemies = []
        for i, j in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            enemy = (pos[0] + i, pos[1] + j)
            if isinstance(self.squares[enemy], target):
                enemies.append((self.squares[enemy].hit, enemy))
        if enemies:
            enemy = sorted(enemies, key=lambda x: (x[0], x[1][1], x[1][0]))[0][1]
            self.squares[enemy].hit -= unit.attack
            if self.squares[enemy].is_dead():
                self.squares[enemy] = '.'

    def turn(self):
        for old_pos, unit in self._get_move_order():
            if self.squares[old_pos] != unit:  # dead this round
                continue
            new_pos = self._get_move(old_pos, unit)
            self._move(unit, old_pos, new_pos)
            self._attack(unit, new_pos)


    def run(self, verbose=False):
        for i in count(1):
            self.turn()
            if verbose:
                print(f"Round {i}\n{self}\n")
            if self._is_finished():
                return self._get_total_hit() * (i - 1)
            

with open("input") as f:
    raw_cave = [line.strip() for line in f.readlines()]

# part I
cave = Cave(raw_cave, elf_attack=3)
print(f"part 1:, {cave.run(True)}")

# part II
elf_attack = 3
while True:
    elf_attack += 1
    cave = Cave(raw_cave, elf_attack=elf_attack)
    n_elves_start = cave.n_units(Elf)
    res = cave.run()
    if n_elves_start == cave.n_units(Elf):
        print(f"part 2: {res}")
        break

