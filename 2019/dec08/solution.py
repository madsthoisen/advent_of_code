import numpy as np


with open("input") as f:
    layers = np.array(list(map(int, f.read().strip()))).reshape(-1, 6, 25)


# part I
layer = layers[(layers == 0).sum(axis=(1, 2)).argmin()]
print((layer == 1).sum() * (layer == 2).sum())

# part II
def f(arr):
    for x in arr:
        if x != 2:
            return x
    return 2
image = np.apply_along_axis(f, 0, layers)
print('\n'.join(''.join(str(x) for x in line).replace('0', ' ') for line in image))
