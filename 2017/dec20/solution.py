import numpy as np

from copy import deepcopy
from itertools import count


with open("input") as f:
	particles_ = [line.strip() for line in f.readlines()]
	particles_ = np.array([np.array([np.array(list(map(int, x[3:-1].split(',')))) for x in particle.split(', ')]) for particle in particles_])


# part I
manh = lambda p: sum(abs(x) for x in p)
particles = deepcopy(particles_)
change, closest = 0, 0
wait = 1000 # no change for 1000 rounds is a choice that works for the input :/
for r in count():
	particles[:, 1] += particles[:, 2]
	particles[:, 0] += particles[:, 1]
	m = [manh(p) for p in particles]
	closest_tmp = np.argmin([manh(p[0]) for p in particles])
	if closest_tmp != closest:
		closest = closest_tmp
	else:
		change += 1
	if change > wait:
		print(closest)
		break

# part II
particles = deepcopy(particles_)
change, prev_len = 0, len(particles)
wait = 1000 # no collision for 1000 rounds is a choice that works for the input :/
for r in count():
	particles[:, 1] += particles[:, 2]
	particles[:, 0] += particles[:, 1]
	unique, counts = np.unique(particles[:, 0], return_counts=True, axis=0)
	occurences = dict(zip([tuple(x) for x in unique], counts))
	indices = [i for i in range(len(particles)) if occurences[tuple(particles[i][0])] == 1]
	particles = particles[indices]
	if (l := len(particles)) < prev_len:
		prev_len = l
	else:
		change += 1
	if change > wait:
		print(l)
		break

