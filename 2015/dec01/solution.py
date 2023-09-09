import numpy as np

with open("input") as f:
    ll = [1 if x == '(' else - 1 for x in f.read().strip()]

# part I
print(sum(ll))

# part II
print(min(np.where(np.cumsum(ll) == -1)) + 1)
