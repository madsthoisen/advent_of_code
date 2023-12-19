from math import prod


with open("input") as f:
    a, b = f.read().split("\n\n")

workflows = {w.split("{")[0]: [x.split(':') for x in w.split("{")[1][:-1].split(',')] for w in a.split()}
ratings = [{x[0]: int(x[2:]) for x in line[1:-1].split(',')} for line in b.split()]


def get(d, wf):
    accepted = []
    new_sends = {}
    *test, rest = workflows[wf]
    for t, otherwise in test:
        cat, compare, num = t[0], t[1], int(t[2:])
        left, right = d[cat]
        d_tmp = dict(d)
        if left < num < right:
            d_tmp[cat] = (left, num - 1) if compare == '<' else (num + 1, right)
            d[cat] = (num, right) if compare == '<' else (left, num)
        if otherwise == 'A':
            accepted.append(d_tmp)
        elif otherwise != 'R':
            new_sends[otherwise] = d_tmp
    if rest[0] == 'A':
        accepted.append(d)
    elif rest[0] != 'R':
        new_sends[rest[0]] = d
    return new_sends, accepted


sends = {'in': {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}}
acc = []
while sends:
    new_sends = {}
    for k, intervals in sends.items():
        ns, accepted = get(intervals, k)
        new_sends.update(ns)
        acc.extend(accepted)
    sends = new_sends

# part I
add = 0
for r in ratings:
    add += sum(sum(r.values()) for a in acc if all(a[x][0] <= r[x] <= a[x][1] for x in ['x', 'm', 'a', 's']))
print(add)


# part II
print(sum(prod(b - a + 1 for a, b in d.values()) for d in acc))
