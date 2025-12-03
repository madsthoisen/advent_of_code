with open("input") as f:
    banks = [list(map(int, line.strip())) for line in f.readlines()]


def check(bank, amnt):
    mi = -1
    res = ''
    for j in range(amnt):
        m = 0
        for i in range(mi + 1, len(bank) - amnt + j + 1):
            val = bank[i]
            if val > m:
                mi, m = i, val
        res += str(m)
    return int(res)


# part I
print(sum(map(lambda x: check(x, 2), banks)))


# part II
print(sum(map(lambda x: check(x, 12), banks)))
