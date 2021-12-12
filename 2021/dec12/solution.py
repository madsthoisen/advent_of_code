from collections import Counter, defaultdict


with open("input") as f:
    lines = [line.strip().split('-') for line in f.readlines()]


edges = defaultdict(set)
for a, b in lines:
    if a != "end" and b != "start":
        edges[a].add(b)
    if b != "end" and a != "start":
        edges[b].add(a)


def count_paths(part2=False):
    paths = [("start",)]
    finished = 0
    while paths:
        path = paths.pop()
        for b in edges[path[-1]]:
            if b in path and b.islower():
                if part2:
                    if any(Counter(path)[x] > 1 for x in path if x.islower()):
                        continue
                else:
                    continue
            if b == 'end':
                finished += 1
            else:
                paths.append(path + (b,))
    return finished


# part I
print(count_paths())

# part II
print(count_paths(True))

