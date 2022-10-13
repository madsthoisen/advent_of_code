from itertools import product


with open("input") as f:
	number = int(f.read())


def get_adj_sum(grid, pos):
	arr = [grid.get((pos[0] + i, pos[1] + j)) for (i, j) in increments]
	return sum(x for x in arr if x)


def inc(p, g, n, x, y, part2):
	p = (p[0] + x, p[1] + y)
	if part2:
		g[p] = get_adj_sum(g, p)
	else:
		g[p] = n + 1
	return p, g, n + 1


def create_grid(n, part2=False):
	pos = (0, 0)
	grid = {pos: 1}
	no, layer = 1, 0
	while True:
		layer += 1
		pos, grid, no = inc(pos, grid, no, 1, 0, part2)
		if grid[pos] > number and part2: return grid[pos]
		# up
		for _ in range(2 * (layer - 1) + 1):
			pos, grid, no = inc(pos, grid, no, 0, 1, part2)
			if grid[pos] > number and part2: return grid[pos]
		# left
		for _ in range(2 * layer):
			pos, grid, no = inc(pos, grid, no, -1, 0, part2)
			if grid[pos] > number and part2: return grid[pos]
		# down
		for _ in range(2 * layer):
			pos, grid, no = inc(pos, grid, no, 0, -1, part2)
			if grid[pos] > number and part2: return grid[pos]
		# right
		for _ in range(2 * layer):
			pos, grid, no = inc(pos, grid, no, 1, 0, part2)
			if grid[pos] > number and part2: return grid[pos]
		if no >= n:
			return grid


increments = list(product([-1, 0, 1], repeat=2))


# part I
grid = create_grid(number)
for pos, val in grid.items():
	if val == number:
		print(abs(pos[0]) + abs(pos[1]))

# part II
print(create_grid(number, True))
