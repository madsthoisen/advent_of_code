with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


p1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
p2 = {'(': 1, '[': 2, '{': 3, '<': 4}
pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}


def score(chunk):
    l = len(chunk) + 1
    while l > len(chunk):
        l = len(chunk)
        for s, e in pairs.items():
            chunk = chunk.replace(s + e, '')
    for i in range(len(chunk) - 1):
        s, e = chunk[i : i + 2]
        if s in pairs and e in pairs.values() and pairs[s] != e:
            return p1[e], True
    score = sum(p2[c] * 5**(len(chunk) - i - 1) for i, c in enumerate(chunk[::-1]))
    return score, False


# part I
print(sum(s for s, corrupted in map(score, lines) if corrupted))

# part II
scores = sorted([s for s, corrupted in map(score, lines) if not corrupted])
print(scores[len(scores) // 2])
