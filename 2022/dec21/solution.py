with open("input") as f:
    lines = [line.strip().split(': ') for line in f.readlines()]


def solve(test=0):
    d = {}
    while True:
        for x, y in lines:
            if x == "humn" and test:
                d[x] = test
                continue
            if y.isdigit():
                d[x] = int(y)
            else:
                a, op, b = y.split(' ')
                if a in d and b in d:
                    if op == '-':
                        d[x] = d[a] - d[b]
                    elif op == '+':
                        d[x] = d[a] + d[b]
                    elif op == '*':
                        d[x] = d[a] * d[b]
                    elif op == '/':
                        d[x] = d[a] / d[b]
                if x == "root" and a in d and b in d:
                    if test:
                        return d[b] - d[a]
                    else:
                        return int(d[x])


# part I
print(solve())

# part II
l, r = 0, 10_000_000_000_000
while True:
    m = (l + r) // 2
    diff = solve(m)
    if diff < 0:
        l = m + 1
    elif diff > 0:
        r = m - 1
    else:
        print(l)
        break

