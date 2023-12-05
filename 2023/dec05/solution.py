from numpy import inf
import portion


class IntInterval(portion.AbstractDiscreteInterval):
    _step = 1


def closed_interval(a, b):
    return IntInterval.from_atomic(portion.CLOSED, a, b, portion.CLOSED)


def increment(interval, x):
    return interval.apply(lambda i: closed_interval(i.lower + x, i.upper + x))


with open("input") as f:
    blocks = [b for b in f.read().split("\n\n") if b != ""]

seeds = list(map(int, blocks[0].split(' ')[1:]))
ranges = []
for x in blocks[1:]:
    tuples = [list(map(int, a.split(' '))) for a in x.split("\n")[1:]]
    d = {closed_interval(src, src + l - 1): dest - src for dest, src, l in tuples}
    ranges.append(d)


def calc(seeds):
    out = inf
    for base, inc in seeds:
        intervals = closed_interval(base, base + inc - 1)
        for v in ranges:
            new_intervals = portion.empty()
            for interval, y in v.items():
                intersection = intervals & interval
                intervals -= intersection
                new_intervals |= increment(intersection, y)
            intervals |= new_intervals
        out = min(min(a.lower for a in intervals), out)
    return out


# part II
print(calc([(x, 1) for x in seeds]))

# part II
print(calc([(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]))
