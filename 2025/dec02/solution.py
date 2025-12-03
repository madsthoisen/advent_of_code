with open("input") as f:
    ranges = [tuple(map(int, r.split('-'))) for r in f.read().split(',')]


def split(pwd, a):
    return [pwd[i:i+a] for i in range(0, len(pwd) - a + 1, a)]


def solve(max_parts):
    add = 0
    for a, b in ranges:
        for p in range(a, b + 1):
            ll = len(str(p))
            for parts in range(2, min(max_parts + 1, ll + 1)):
                if not ll % parts and len(set(split(str(p), ll // parts))) == 1:
                    add += p
                    break
    return add


# part I
print(solve(2))

# part II
print(solve(999))
