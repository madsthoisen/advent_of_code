from itertools import permutations


with open("input") as f:
    operations = [line.strip().split(' ') for line in f.readlines()]


def scramble(pwd):
    l = len(pwd)
    for op in operations:
        if op[0] == 'swap':
            c1, c2 = op[2], op[-1]
            if op[1] == 'position':
                c1, c2 = pwd[int(c1)], pwd[int(c2)]
            new_pwd = pwd.translate({ord(c1): c2, ord(c2): c1})

        if op[0] == 'move':
            p1, p2 = int(op[2]), int(op[-1])
            new_pwd = pwd[:p1] + pwd[p1 + 1:]
            new_pwd = new_pwd[:p2] + pwd[p1] + new_pwd[p2:]

        if op[0] == 'rotate':
            if op[1] == 'based':
                r = pwd.index(op[-1])
                r = r + 2 if r > 3 else r + 1
                r %= l
                direction = 'right'
            else:
                r = int(op[2])
                direction = op[1]
            if direction == 'left':
                new_pwd = pwd[r:] + pwd[:r:]
            if direction == 'right':
                new_pwd = pwd[-r:] + pwd[:-r]

        if op[0] == 'reverse':
            p1, p2 = int(op[2]), int(op[4])
            new_pwd = pwd[:p1] + pwd[p1:p2 + 1][::-1] + pwd[p2 + 1:]
        pwd = new_pwd
    return pwd
        

# part I
print(scramble("abcdefgh"))

# part II
for pwd in permutations("abcdefgh", 8):
    pwd = ''.join(pwd)
    if scramble(pwd) == "fbgdceah":
        print(pwd)
