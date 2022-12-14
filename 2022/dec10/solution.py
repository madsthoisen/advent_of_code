with open("input") as f:
    ops = [line.strip().split(' ') for line in f.readlines()]

x = 1
c = 0
add = 0
col = 0
disp = ""
for op in ops:
    time = 1 if op[0] == 'noop' else 2
    val = int(0 if op[0] == 'noop' else int(op[1]))
    for _ in range(time):
        disp = disp + '#' if col in [x - 1, x, x + 1] else disp + '.'
        c += 1
        if c in [20, 60, 100, 140, 180, 220]:
            add += int(c * x)
        col = (col + 1) % 40
    x += val

# part I
print(add)

# part II
for i in range(6):
    print(disp[40*i:40*(i + 1)])
