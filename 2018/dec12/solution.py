with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]


def next_generation(state, instructions, first_index):
    while state[:3] != '...':
        state = '.' + state
        first_index -= 1
    while state[-3:] != '...':
        state += '.'
    new_state = state[:2]
    for i in range(2, len(state) - 2):
        s = state[i - 2 : i + 3]
        new_state += instructions[s]
    return new_state + state[-2:], first_index


# part I
state = tmp[0].split(': ')[1]
instructions = {l.split(' => ')[0]: l.split(' => ')[1] for l in tmp[2:]}
first_index = 0
for _ in range(20):
    state, first_index = next_generation(state, instructions, first_index)
print(sum(i + first_index for i, s in enumerate(state) if s == '#'))

# part II
state = tmp[0].split(': ')[1]
first_index = 0
for i in range(1, 1001):
    state, first_index = next_generation(state, instructions, first_index)
    reduced_state = state
    first_flower = first_index
    while reduced_state[0] == '.':
        reduced_state = reduced_state[1:]
        first_flower += 1
    diff = i - first_flower
    print(i, first_flower, diff, sum(i + first_index for i, s in enumerate(state) if s == '#'))
print(sum(i + 50000000000 - diff for i, s in enumerate(reduced_state) if s == '#'))
