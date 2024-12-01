with open("input") as f:
    lines = [map(int, line.strip().split()) for line in f.readlines()]


la, lb = list(zip(*lines))


# Part I
print(sum(abs(a - b) for a, b in zip(sorted(la), sorted(lb))))


# Part II
print(sum(a * lb.count(a) for a in la))
