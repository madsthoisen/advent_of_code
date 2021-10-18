from collections import defaultdict


with open("input") as f:
	instructions = [line.strip() for line in f.readlines()]


reg = defaultdict(int)
m = -999
for instruction in instructions:
	ins, cond = instruction.split(" if ")
	pos, way, val = ins.split(" ")
	l, expr, r = cond.split(" ")
	if eval("reg[l]" + expr + "int(r)"):
		if way == "inc":
			reg[pos] += int(val)
		else:
			reg[pos] -= int(val)
	m = max(m, max(reg.values()))


# part I
print(max(reg.values()))

# part II
print(m)
