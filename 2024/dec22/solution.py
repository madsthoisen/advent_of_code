from collections import defaultdict


with open("input") as f:
    numbers = list(map(int, f.read().split("\n")))


def do(n):
    m = 2**24
    n = (n * 2**6 ^ n) % m
    n = (n // 2**5 ^ n) % m
    return (n * 2**11 ^ n) % m


dd = defaultdict(int)
add = 0
for num in numbers:
    vals = [num % 10] + [(num := do(num)) % 10 for _ in range(2000)]
    changes = [b - a for a, b in zip(vals, vals[1:])]
    seen = set()
    for i in range(4, len(changes)):
        if (t := tuple(changes[i - 4: i])) not in seen:
            seen.add(t)
            dd[t] += vals[i]
    add += num

# part I
print(add)

# part II
print(max(dd.values()))
