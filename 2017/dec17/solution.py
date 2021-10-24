steps = 303 # input


# part I
pos = 0
circular_buffer = [0]
for insertion in range(1, 2017 + 1):
	pos = (pos + steps) % len(circular_buffer)
	circular_buffer = circular_buffer[:pos + 1] + [insertion] + circular_buffer[pos + 1:]
	pos += 1

print(circular_buffer[(pos + 1) % len(circular_buffer)])

# part II
pos = 0
for i in range(1, 50_000_000 + 1):
	if (pos := (pos + steps) % i + 1)== 1:
		out = i

print(out)
