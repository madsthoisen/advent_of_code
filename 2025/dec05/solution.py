with open("input") as f:
    ranges, available = f.read().split("\n\n")

ranges = sorted([list(map(int, r.split('-'))) for r in ranges.split("\n")])
available = list(map(int, available.split("\n")))


def check(ing):
    for a, b in ranges:
        if a <= ing <= b:
            return True
    return False


# part I
print(sum(check(ing) for ing in available))

# part II
i = 0
while i < len(ranges) - 1:
    a, b = ranges[i]
    c, d = ranges[i + 1]
    if c <= b:
        ranges[i] = [a, max(b, d)]
        del ranges[i + 1]
    else:
        i += 1
print(sum(b - a + 1 for a, b in ranges))
