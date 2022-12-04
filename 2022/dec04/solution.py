with open("input") as f:
    intervals = [[tuple(map(int, s.split('-'))) for s in line.strip().split(',')] for line in f.readlines()]


def sr(a):
    return set(range(a[0], a[1] + 1))


# part I
print(sum(sr(a).issubset(sr(b)) or sr(b).issubset(sr(a)) for a, b in intervals))

# part II
print(sum(len(sr(a) & sr(b)) > 0 for a, b in intervals))