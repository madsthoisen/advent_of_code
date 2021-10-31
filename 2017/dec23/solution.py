from sympy import isprime


with open("input") as f:
	instructions = [line.strip().split(' ') for line in f.readlines()]

# part I
registers = {chr(97 + i): 0 for i in range(8)}

i = 0
count = 0
while True:
	if i >= len(instructions):
		print(count)
		break
	cmd, x, y = instructions[i]
	try:
		y = int(y)
	except:
		y = int(registers[y])
	if cmd == 'set':
		registers[x] = y
	elif cmd == 'sub':
		registers[x] -= y
	elif cmd == 'mul':
		registers[x] *= y
		count += 1
	elif cmd == 'jnz':
		try:
			x = int(x)
		except:
			x = int(registers[x])
		if x != 0:
			i += y
			continue
	i += 1

# part II
print(sum(not isprime(x) for x in range(107900, 124900 + 1, 17)))
