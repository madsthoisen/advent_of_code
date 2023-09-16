with open("input") as f:
    tmp = [line.strip().replace(',', '').replace(':', '').split() for line in f.readlines()]
    sues = {x[1]: {x[2]: int(x[3]), x[4]: int(x[5]), x[6]: int(x[7])} for x in tmp}

ticker_tape = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
               "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}


def validate(thing, n, part2=False):
    t = ticker_tape.get(thing)
    if part2:
        if thing in {"cats", "trees"}:
            return n >= t
        if thing in {"goldfish", "pomerians"}:
            return n <= t
    return n == t


# part I
print(next(sue for sue, things in sues.items() if all(validate(thing, n) for thing, n in things.items())))

# part II
print(next(sue for sue, things in sues.items() if all(validate(thing, n, True) for thing, n in things.items())))
