from collections import defaultdict
from itertools import count


with open("input") as f:
	instructions = [line.strip().split(' ') for line in f.readlines()]

# part I
reg = defaultdict(int)
pos = 0
while True:
	instruction = instructions[pos]
	i = instruction[0]
	x = instruction[1]
	if i not in {'snd', 'rcv'}:
		y = instruction[2]
		try:
			y = int(y)
		except:
			y = reg[y]
	if i == 'snd':
		sound = reg[x]
	elif i == 'set':
		reg[x] = y
	elif i == 'add':
		reg[x] += y
	elif i == 'mul':
		reg[x] *= y
	elif i == 'mod':
		reg[x] %= y
	elif i == 'rcv':
		if reg[x] != 0:
			rcv = sound
			print(rcv)
			break
	elif i == 'jgz':
		if reg[x] > 0:
			pos += y
			continue
	pos += 1


# part II
def program(program_id, instructions):
	send_count = 0
	reg = defaultdict(int)
	reg['p'] = program_id
	pos = 0
	while True:
		instruction = instructions[pos]
		i = instruction[0]
		x = instruction[1]
		if i not in {'snd', 'rcv'}:
			y = instruction[2]
			try:
				y = int(y)
			except:
				y = reg[y]
		if i == 'snd':
			send_count += 1
			q[1 - program_id].append(reg[x])
		elif i == 'set':
			reg[x] = y
		elif i == 'add':
			reg[x] += y
		elif i == 'mul':
			reg[x] *= y
		elif i == 'mod':
			reg[x] %= y
		elif i == 'rcv':
			while not q[program_id]:
				yield send_count
			else:
				reg[x] = q[program_id].pop(0)
		elif i == 'jgz':
			try:
				x = int(x)
			except:
				x = reg[x]
			if x > 0:
				pos += y
				continue
		pos += 1

# so dirty manipulating global variables inside method
program_0 = program(0, instructions)
program_1 = program(1, instructions)
q = [[], []]

for i in count():
	next(program_0)
	send_count = next(program_1)
	if len(q[0]) == 0 and len(q[1]) == 0 and i > 1:
		print(send_count)
		break

