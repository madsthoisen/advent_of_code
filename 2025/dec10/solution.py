from itertools import count
from scipy.optimize import linprog


with open("input") as f:
    lines = [line.strip().split(' ') for line in f.readlines()]


def bfs(ind, buttons):
    states = [ind]
    for presses in count(1):
        new_states = set()
        for state in states:
            for button in buttons:
                new_state = tuple([(x + y) % 2 for x, y in zip(state, button)])
                if all(x == 0 for x in new_state):
                    return presses
                new_states.add(new_state)
        states = new_states


def ip(buttons, jolt):
    A = list(map(list, zip(*buttons)))
    c = [1 for _ in range(len(A[0]))]
    b = list(jolt)
    res = linprog(c, A_eq=A, b_eq=b, integrality=1)
    return sum(res.x)


p1, p2 = 0, 0
for line in lines:
    ind = [int(x == '#') for x in line[0][1:-1]]
    buttons = [set(map(int, x[1:-1].split(','))) for x in line[1:-1]]
    buttons = [[int(i in button) for i in range(len(ind))] for button in buttons]
    p1 += bfs(ind, buttons)
    jolt = map(int, line[-1][1:-1].split(','))
    p2 += ip(buttons, jolt)

# part I
print(p1)

# part II
print(int(p2))
