import numpy as np


with open("input") as f:
    numbers = np.array(list(map(int, f.read().strip().split(','))))


m, M = min(numbers), max(numbers)
distances = np.array([abs(numbers - p) for p in range(m, M)])

# part I
print(min(distances.sum(1)))

# part II
distances = (distances**2 + distances) // 2
print(min(distances.sum(1)))
