with open("input") as f:
    tmp = [line.strip().split(' ') for line in f.readlines()]
    specs = {x[0]: [int(x[3]), int(x[6]), int(x[13])] for x in tmp}  # flight speed, flight time, rest time

reindeers = {k: [0, s[1], 0, 0] for k, s in specs.items()}  # total travelled, flight time left, time rested, points

for _ in range(2503):
    for k, v in reindeers.items():
        if v[2] > 0:
            v[2] -= 1
        else:
            v[1] -= 1
            v[0] += specs[k][0]
        if v[1] == 0:
            v[1:3] = specs[k][1:3]
    for k, v in reindeers.items():
        v[3] += v[0] == max(x[0] for x in reindeers.values())


# part I
print(max(v[0] for v in reindeers.values()))

# part I
print(max(v[3] for v in reindeers.values()))
