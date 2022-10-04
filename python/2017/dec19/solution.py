from itertools import count


with open("input") as f:
	diagram = [line.strip("\n") for line in f.readlines()]


h, w = len(diagram), len(diagram[0])
pos = [0, diagram[0].index("|")]
direction = 'd'
letters = []
for c in count():
	symbol = diagram[pos[0]][pos[1]]
	if not (0 <= pos[0] <= w) or not (0 <= pos[1] <= h) or symbol == ' ':
		break
	if symbol == '+':
		if direction in {'d', 'u'}:
			if pos[1] > 0 and diagram[pos[0]][pos[1] - 1] != ' ':
				pos[1] -= 1
				direction = 'l'
			elif pos[1] < w and diagram[pos[0]][pos[1] + 1] != ' ':
				pos[1] += 1
				direction = 'r'
		elif direction in {'l', 'r'}:
			if pos[0] > 0 and diagram[pos[0] - 1][pos[1]] != ' ':
				pos[0] -= 1
				direction = 'u'
			elif pos[1] < w and diagram[pos[0] + 1][pos[1]] != ' ':
				pos[0] += 1
				direction = 'd'
	else:
		if direction == 'd':
			pos[0] += 1
		if direction == 'u':
			pos[0] -= 1
		if direction == 'l':
			pos[1] -= 1
		if direction == 'r':
			pos[1] += 1
		if symbol not in {'|', '-'}:
			letters.append(symbol)
# part I
print(''.join(letters))

# part II
print(c)
