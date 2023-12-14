from collections import defaultdict


with open("input") as f:
    lines = [line.strip().split(' ') for line in f.readlines()]


def is_valid(a, b):
    res = [len(x) for x in a.split('.')]
    exp = list(map(int, b.split(',')))
    return res == exp


def clean(a):
    if len(a) < 2:
        return a
    while a[0] == '.':
        a = a[1:]
    while a[-1] == '.':
        a = a[:-1]
    while '..' in a:
        a = a.replace('..', '.')
    return a


def solve(a, b):
    curr = defaultdict(int, {a: 1})
    add = 0
    while curr:
        new_curr = defaultdict(int)
        for xx, val in curr.items():
            if '?' in xx:
                i = next(i for i, x in enumerate(xx) if x == '?')
                one = clean(xx[:i] + '#' + xx[i + 1:])
                two = clean(xx[:i] + '.' + xx[i + 1:])
                if feasible(one, b):
                    new_curr[one] += val
                if feasible(two, b):
                    new_curr[two] += val
            else:
                if is_valid(xx, b):
                    add += val
        curr = new_curr
    return add


def feasible(a, b):
    blist = list(map(int, b.split(',')))
    a = clean(a)
    blocks = []
    curr = ''
    type = -1
    for x in a:
        new_type = 0 if x in {'.', '?'} else 1
        if new_type == type or type == -1:
            curr += x
        else:
            blocks.append(curr)
            curr = x
        type = new_type

    if curr:
        blocks.append(curr)
    largest_block = max(blist)
    if any(b.count('#') > largest_block for b in blocks):
        return False
    if a.count('#') > sum(blist):
        return False
    if blocks[0].count('#') > blist[0]:
        return False
    if '?' in a:
        i = next(i for i, x in enumerate(a) if x == '?')
        done_part = [len(x) for x in a[:i].split('.')]
        if any(x != y for x, y in zip(done_part[:-1], blist)):
            return False
        if any(x > y for x, y in zip(done_part, blist)):
            return False
    return True


# part I
print(sum(solve(a, b) for a, b in lines))  # 7169

# part II
lines = [('?'.join(a for _ in range(5)), ','.join(b for _ in range(5))) for a, b in lines]
print(sum(solve(a, b) for a, b in lines))  # 1738259948652
