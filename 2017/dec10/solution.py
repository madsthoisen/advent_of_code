from functools import reduce


with open("input") as f:
	lengths_str = f.read().strip()
	lengths_int = [int(x) for x in lengths_str.split(',')]

def run(numbers, lengths, rounds):
	l = len(numbers)
	pos, skip_size = 0, 0
	for _ in range(rounds):
		for length in lengths:
			tmp = []
			for i in range(length):
				tmp.append(numbers[(pos + i) % l])
			tmp = tmp[::-1]
			for i in range(length):
				numbers[(pos + i) % l] = tmp.pop(0)
			pos = (pos + length + skip_size) % l
			skip_size += 1
	return numbers

# part I
numbers = run(list(range(256)), lengths_int, 1)
print(numbers[0] * numbers[1])

# part II
lengths = [ord(c) for c in lengths_str] + [17, 31, 73, 47, 23]
numbers = run(list(range(256)), lengths, 64)
L = [reduce(lambda x, y: x ^ y, numbers[16 * i : 16 * i + 16]) for i in range(16)]
print(''.join([hex(x)[2:].zfill(2) for x in L]))
