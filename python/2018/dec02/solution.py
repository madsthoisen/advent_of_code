from collections import Counter


with open("input") as f:
    candidates = [l.strip() for l in f.readlines()]


# part I
twos, threes = 0, 0
for candidate in candidates:
    counts = Counter(candidate)
    twos += int(2 in counts.values())
    threes += int(3 in counts.values())
print(twos * threes)

# part II
for i, candidate in enumerate(candidates):
    for j in range(i + 1, len(candidates)):
        if sum(a != b for a, b in zip(candidate, candidates[j])) == 1:
            print(''.join(a for a, b in zip(candidate, candidates[j]) if a == b))
