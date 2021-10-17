with open("input") as f:
	num = f.read().strip()


l = len(num)

# part 1
print(sum([int(x) for idx, x in enumerate(num) if num[(idx + 1) % l] == x]))

# part 2
print(sum([int(x) for idx, x in enumerate(num) if num[(idx + l // 2) % l] == x]))
