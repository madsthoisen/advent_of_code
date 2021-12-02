with open("input") as f:
    commands = [line.strip().split(' ') for line in f.readlines()]


# part I
dep, hor = 0, 0
for command, val in commands:
    val = int(val)
    if command == 'up':
        dep -= val
    if command == 'down':
        dep += val
    if command == 'forward':
        hor += val 
print(hor * dep)


# part II
dep, hor, aim = 0, 0, 0
for command, val in commands:
    val = int(val)
    if command == 'up':
        aim -= val
    if command == 'down':
        aim += val
    if command == 'forward':
        hor += val 
        dep += (aim * val)
print(hor * dep)
