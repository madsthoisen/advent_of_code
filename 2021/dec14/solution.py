from collections import defaultdict


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


word = lines[0]
s = {(w := word[i : i + 2]): word.count(w) for i in range(len(word) - 1)}
rules = dict(line.split(' -> ') for line in lines[2:])


def step(s):
    new_s = defaultdict(int)
    for k in s:
        if k in rules:
            new_s[k[0] + rules[k]] += s[k]
            new_s[rules[k] + k[1]] += s[k]
        else:
            new_s[k] = 1
    return new_s


def get_answer(n_steps, s):
    for _ in range(n_steps):
        s = step(s)
    
    counts = defaultdict(int)
    for w, v in s.items():
        counts[w[0]] += v
        counts[w[1]] += v
    counts = {k: v // 2 if k not in {word[0], word[1]} else v // 2 + 1 for k, v in counts.items()}
    return max(counts.values()) - min(counts.values())


# part I
print(get_answer(10, s))

# part II
print(get_answer(40, s))
