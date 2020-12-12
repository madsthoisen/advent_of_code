with open("input") as f:
    L = [l.strip().split() for l in f.readlines()]

def get(arr):
    s, e = list(map(int, arr[0].split('-')))
    l = arr[1][0]
    pwd = arr[2]
    return s, e, l, pwd

def part1(arr):
    s, e, l, pwd = get(arr)
    return (s <= pwd.count(l) <= e)

def part2(arr):
    s, e, l, pwd = get(arr)
    b1 = False if s > len(pwd) else pwd[s - 1] == l
    b2 = False if e > len(pwd) else pwd[e - 1] == l
    return b1 + b2 == 1

print(sum(list(map(part1, L))))
print(sum(list(map(part2, L))))
