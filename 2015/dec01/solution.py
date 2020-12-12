import numpy as np

with open("input") as f:
    app = f.read().strip()

# part I
print(app.count('(') - app.count(')'))

# part II
L = [1 if a == '(' else -1 for a in app]
print(np.where(np.cumsum(L) == -1)[0][0] + 1)
