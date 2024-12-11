from collections import defaultdict


with open("input") as f:
    stones = {s: 1 for s in map(int, f.read().strip().split())}


def grow(stones):
    ns = defaultdict(int)
    for s, amnt in stones.items():
        ss = str(s)
        if s == 0:
            ns[1] += amnt
        elif (ll := len(ss)) % 2 == 0:
            ns[int(ss[:ll // 2])] += amnt
            ns[int(ss[ll // 2:])] += amnt
        else:
            ns[s * 2024] += amnt
    return ns


# part I
for _ in range(25):
    stones = grow(stones)
print(sum(stones.values()))

# part II
for _ in range(50):
    stones = grow(stones)
print(sum(stones.values()))
