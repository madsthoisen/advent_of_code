from collections import defaultdict, Counter


with open("input_test") as f:
    strings = [line.strip() for line in f.readlines()]


d = {}
curr = d
i = 0
while i < len(strings):
    l = strings[i].split(' ')
    assert l[0] == '$'
    if l[1] == 'ls':
        while True:
            i += 1
            if i >= len(strings):
                break
            l = strings[i].split(' ')
            if l[0] == '$':
                break
            if l[0] == 'dir':
                curr[l[1]] = {}
                pass
            else:
                curr[l[1]] = int(l[0])

    elif l[1] == 'cd':
        a = l[2]
        if a == '/':
            curr = d
        elif a == '..':
            curr = prev
        else:
            if a not in curr:
                curr[a] = {}
            prev = curr
            curr = curr[a]
        i += 1
    else:
        assert False

vals = defaultdict(int)
def get_vals(d, name):
    vals[name] = get_all_filesums(d)
    for k, v in d.items():
        print(k, v)
        if isinstance(v, dict):
            get_vals(v, k)


def get_all_filesums(d, total=0):
    if isinstance(d, int):
        return d
    for k, v in d.items():
        total += get_all_filesums(v)
    return total

print(d)
assert False
vals = get_vals(d, 'root')
add = 0
for k, v in vals.items():
    if v <= 100_000:
        add += v

# 495837 is too low