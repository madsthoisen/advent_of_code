from collections import defaultdict, Counter


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


word = lines[0]
pairs = Counter(u + v for u, v in zip(word, word[1:]))
chars = Counter(word)
rules = dict(line.split(' -> ') for line in lines[2:])


def step(n):
    for _ in range(n):
        for k, v in pairs.copy().items():
            assert k in rules
            pairs[k[0] + rules[k]] += v
            pairs[rules[k] + k[1]] += v 
            chars[rules[k]] += v
            pairs[k] -= v
    return max(chars.values()) - min(chars.values())


# part I
print(step(10))

# part II
print(step(30))

