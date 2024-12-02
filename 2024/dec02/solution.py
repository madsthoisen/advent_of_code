with open("input") as f:
    reports = [list(map(int, line.strip().split())) for line in f.readlines()]


def safe(rep):
    for sgn in [-1, 1]:
        if all(sgn * (y - x) in {1, 2, 3} for x, y in zip(rep, rep[1:])):
            return True
    return False


# part I
print(sum(safe(rep) for rep in reports))


# part II
print(sum(any(safe(rep[:i] + rep[i + 1:]) for i in range(-1, len(rep) + 1)) for rep in reports))
