with open("input") as f:
    reports = [list(map(int, line.split())) for line in f.readlines()]


def safe(rep):
    for sgn in [-1, 1]:
        if all(sgn * (y - x) in {1, 2, 3} for x, y in zip(rep, rep[1:])):
            return True
    return False


# part I
print(sum(map(safe, reports)))


# part II
print(sum(any(safe(rep[:i] + rep[i + 1:]) for i in range(len(rep))) for rep in reports))
