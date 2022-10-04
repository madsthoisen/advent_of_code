with open("input") as f:
    ins = f.read().strip().split(', ')

pos = 0
positions = {pos}
part2 = 0
d = 1j
for el in ins:
    r, l = el[0], int(el[1:])
    if r == 'R':
        d *= -1j
    elif r == 'L':
        d *= 1j
    for _ in range(l):
        pos += d
        if pos in positions and not part2:
            part2 = pos
        positions.add(pos)

# part I
print(int(abs(pos.real) + abs(pos.imag)))

# part II
print(int(abs(part2.real) + abs(part2.imag)))
