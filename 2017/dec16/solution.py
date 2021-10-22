with open("input") as f:
	dance = f.read().strip().split(',')


def dance_rounds(n, n_programs=16):
	programs = {chr(97 + i): i for i in range(n_programs)}
	seen = {}
	for r in range(1, n + 1):
		for d in dance:
			if d[0] == 's':
				spin = int(d[1:])
				for p in programs:
					programs[p] = (programs[p] + spin) % n_programs
			if d[0] == 'x':
				a, b = map(int, d[1:].split('/'))
				for k, v in programs.items():
					if v == a:
						key_a = k
					if v == b:
						key_b = k
				programs[key_a], programs[key_b] = b, a
			if d[0] == 'p':
				a, b = d[1:].split('/')
				programs[a], programs[b] = programs[b], programs[a]
		# if the thing is cyclic, be smart:
		if (s := ''.join([x[1] for x in sorted([(v, k) for k, v in programs.items()])])) in seen:
			return dance_rounds(n % (r - seen[s]), n_programs)
		seen[s] = r
	return ''.join([x[1] for x in sorted([(v, k) for k, v in programs.items()])])

# part I
print(dance_rounds(1))

# part II
print(dance_rounds(1_000_000_000))
