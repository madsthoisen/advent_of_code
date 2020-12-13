import re

with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]

patterns = [r"\\x[0-9a-fA-F]{2}", r"\\\\", r"\\\""]

# part I
add = 0
for line in tmp:
    l = len(line)
    for pattern in patterns:
        line = re.sub(pattern, "x", line)
    line = line[1:-1]
    add += (l - len(line)) 
print(add)

# part II
add = 0
for line in tmp:
    l = len(line)
    line = re.sub(patterns[0], "xxxxx", line)
    line = re.sub(patterns[1], "xxxx", line)
    line = re.sub(patterns[2], "xxxx", line)
    add += (len(line) + 4 - l) 
print(add)
