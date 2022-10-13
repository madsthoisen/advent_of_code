from itertools import count


with open("input") as f:
	a, b = [int(line.strip().split(' ')[-1]) for line in f.readlines()]


def next_number(num, factor):
	return (num * factor) % 2_147_483_647


factor_a, factor_b = 16807, 48271
pairs_part_1 = 40_000_000
pairs_part_2 = 5_000_000
count_part_1 = 0
a_values, b_values = [], []
for i in count():
	if not a % 4:
		a_values.append(a)
	if not b % 8:
		b_values.append(b)
	if bin(a).zfill(16)[-16:] == bin(b).zfill(16)[-16:] and i <= pairs_part_1:
		count_part_1 += 1
	a = next_number(a, factor_a)
	b = next_number(b, factor_b)
	if len(a_values) > pairs_part_2 and len(b_values) > pairs_part_2:
		break

# part I
print(count_part_1)

# part II
count_part_2 = 0
for a, b in zip(a_values[:pairs_part_2], b_values[:pairs_part_2]):
	if bin(a).zfill(16)[-16:] == bin(b).zfill(16)[-16:]:
		count_part_2 += 1
print(count_part_2)
