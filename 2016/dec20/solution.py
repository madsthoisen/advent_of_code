with open("input") as f:
    ip_ranges = sorted([list(map(int, line.strip().split('-'))) for line in f.readlines()])


end_range = 4294967295
e_prev = 0
add = 0
part_1 = False
for s, e in ip_ranges:
    e = max(e, e_prev)
    if s > e_prev + 1:
        if not part_1:
            part_1 = e_prev + 1
        add += (s - e_prev - 1)
    e_prev = e

# part I
print(part_1)

# part II
print(add + (end_range - e))
