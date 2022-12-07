with open("input") as f:
    strings = [line.strip().split(' ') for line in f.readlines()][::-1]


root = {}
curr = root
prev = []
l = strings.pop()
while strings:
    if l[1] == 'ls':
        while strings:
            l = strings.pop()
            if l[0] == '$':
                break
            elif l[0] == 'dir':
                if l[1] not in curr:
                    curr[l[1]] = {}
            else:  # file
                curr[l[1]] = int(l[0])

    elif l[1] == 'cd':
        a = l[2]
        if a == '/':
            curr = root
            prev = []
        elif a == '..':
            curr = prev.pop()
        else:
            if a not in curr:
                curr[a] = {}
            prev.append(curr)
            curr = curr[a]
        l = strings.pop()


def get_dirsize(d):
    if isinstance(d, int):
        return d
    return sum(get_dirsize(v) for k, v in d.items())


def get_sizes(d):
    sums.append(get_dirsize(d))
    for dir_name, dir_dict in d.items():
        if isinstance(dir_dict, dict):
            get_sizes(dir_dict)
    return sums


# part I
sums = []
get_sizes(root)
print(sum(x for x in sums if x <= 100000))

# part II
print(min(x for x in sums if 70_000_000 - (get_dirsize(root) - x) >= 30_000_000))