import re

from itertools import count


n_recipes = 505961


current = "37"
a, b = 0, 1
part_1 = False
while True:
    c_a, c_b = int(current[a]), int(current[b])
    current += str(c_a + c_b)
    l = len(current)
    a, b = (1 + c_a + a) % l, (1 + c_b + b) % l
    if l >= n_recipes + 10 and not part_1:
        # part I
        print(''.join([current[i] for i in range(n_recipes, n_recipes + 10)]))
        part_1 = True
    if str(n_recipes) in current[-8:]:
        # part II
        print(re.search(str(n_recipes), current).span()[0])
        break



