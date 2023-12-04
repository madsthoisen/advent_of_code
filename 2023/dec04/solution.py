from collections import defaultdict


with open("input") as f:
    lines = [line.strip().split(': ') for line in f.readlines()]

add = 0
nums = defaultdict(lambda: 1)
for c, rest in lines:
    c = int(c[5:])
    if c not in nums:
        nums[c] = 1
    a, b = rest.split(' | ')
    w = len(set(map(int, a.split())) & set(map(int, b.split())))
    for no in range(c + 1, c + 1 + w):
        nums[no] += nums[c]
    count = 1 if w else 0
    for _ in range(w - 1):
        count *= 2
    add += count

# part I
print(add)

# part II
print(sum(nums.values()))
