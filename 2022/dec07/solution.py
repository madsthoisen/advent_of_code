with open("input") as f:
    lines = [line.strip().split(' ') for line in f.readlines()]


root = {}
curr = root
prev = []
for l in lines:
    if l[1] == 'cd':
        if l[2] == '/':
            curr, prev = root, []
        elif l[2] == '..':
            curr = prev.pop()
        else:
            prev.append(curr)
            curr = curr[l[2]]
    elif l[1] == 'ls':
        pass
    else:
        if l[0] == 'dir' and l[1] not in curr:
            curr[l[1]] = {}
        else:
            curr[l[1]] = int(l[0])


def get_dirsize(d):
    if isinstance(d, int):
        return d
    return sum(get_dirsize(v) for k, v in d.items())


def get_sizes(d):
    sums.append(get_dirsize(d))
    for dir_name, dir_dict in d.items():
        if isinstance(dir_dict, dict):
            get_sizes(dir_dict)


# part I
sums = []
get_sizes(root)
print(sum(x for x in sums if x <= 100000))

# part II
print(min(x for x in sums if 70_000_000 - (get_dirsize(root) - x) >= 30_000_000))
