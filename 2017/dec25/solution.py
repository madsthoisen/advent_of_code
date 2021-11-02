from collections import defaultdict


def f(state, p):
    if state == 'a':
        if tape[p] == 0:
            tape[p] = 1
            return 'b', p + 1
        else:
            tape[p] = 0
            return 'c', p - 1
    if state == 'b':
        if tape[p] == 0:
            tape[p] = 1
            return 'a', p - 1
        else:
            return 'c', p + 1
    if state == 'c':
        if tape[p] == 0:
            tape[p] = 1
            return 'a', p + 1
        else:
            tape[p] = 0
            return 'd', p - 1
    if state == 'd':
        if tape[p] == 0:
            tape[p] = 1
            return 'e', p - 1
        else:
            return 'c', p - 1
    if state == 'e':
        if tape[p] == 0:
            tape[p] = 1
            return 'f', p + 1
        else:
            return 'a', p + 1
    if state == 'f':
        if tape[p] == 0:
            tape[p] = 1
            return 'a', p + 1
        else:
            return 'e', p + 1

# part I
tape = defaultdict(int)
state = 'a'
p = 0
for _ in range(12261543):
    state, p = f(state, p)
print(sum(tape.values()))
