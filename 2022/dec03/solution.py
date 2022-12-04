with open("input") as f:
    ss = [line.strip() for line in f.readlines()]


def val(l):
    return ord(l) - 96 if l.islower() else ord(l) - 38


# part I
print(sum(sum(map(val, set(s[: len(s) // 2]) & set(s[len(s) // 2:]))) for s in ss))

# part II
print(sum(sum(map(val, set(ss[i]) & set(ss[i + 1]) & set(ss[i + 2]))) for i in range(0, len(ss) - 2, 3)))