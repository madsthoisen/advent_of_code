from itertools import permutations

with open("input") as f:
	spreadsheet = [list(map(int, l.strip().split('\t'))) for l in f.readlines()]

# part I
print(sum(max(l) - min(l) for l in spreadsheet))

# part II
print(sum(i // j for l in spreadsheet for i, j in permutations(l, 2) if (i / j).is_integer()))
