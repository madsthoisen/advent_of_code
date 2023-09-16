from itertools import product


with open("input") as f:
    containers = list(map(int, f.readlines()))

bins = product([0, 1], repeat=len(containers))
valid = {b: sum(b) for b in bins if sum(containers[i] for i, val in enumerate(b) if val) == 150}

# part I
print(len(valid))

# part II
print(sum(v == min(valid.values()) for k, v in valid.items()))
