def is_open(x, y, num):
    return not str(bin(x*x + 3*x + 2*x*y + y + y*y + num)).count('1') % 2


INPUT_NUM = 1364


stack = [(1, 1)]
visited = {(1, 1)}
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
part_1 = False
i = 1
while not part_1 or i < 51:
    new_stack = []
    while stack:
        x, y = stack.pop()
        for d in dirs:
            tmp = (x + d[0], y + d[1])
            if tmp[0] < 0 or tmp[1] < 0:
                continue
            if is_open(tmp[0], tmp[1], INPUT_NUM):
                if tmp not in visited:
                    visited.add(tmp)
                    new_stack.append(tmp)
                    if tmp == (31, 39) and not part_1:
                        part_1 = i
    if i == 50:
        part_2 = len(visited)
    stack = new_stack
    i += 1

# part I
print(part_1)

# part II
print(part_2)
