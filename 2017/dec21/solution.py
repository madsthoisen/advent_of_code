import numpy as np


with open("input") as f:
	program = [line.strip().split(' => ') for line in f.readlines()]


def t(im):
	return tuple([tuple(x) for x in im])


def construct_matrix(dic, n_rows, n_cols):
		return np.vstack([np.hstack([dic[(i, j)] for j in range(n_cols)]) for i in range(n_rows)])

program = {t(k.split('/')): t(v.split('/')) for k, v in program}
image = np.array([list(x) for x in ['.#.', '..#', '###']])

def run(n_rounds, program, image):
	for _ in range(n_rounds):
		size = len(image)
		div = 2 if not size % 2 else 3
		new = {}
		for i in range(0, size, div):
			for j in range(0, size, div):
				sub_im = image[i : i + div, j : j + div]
				for _ in range(4):
					if (tup := t(sub_im)) in program:
						new[(i // div, j // div)] = program[tup]
						break
					elif (tup := t(sub_im.transpose())) in program:
						new[(i // div, j // div)] = program[tup]
						break
					sub_im = np.rot90(sub_im)

		image = construct_matrix(new, size // div, size // div)
	
	unique, counts = np.unique(image, return_counts=True)
	return dict(zip(unique, counts))['#']

# part I
print(run(5, program, image))


## part II
print(run(18, program, image))
