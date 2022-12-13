with open("input") as f:
    blocks = f.read().split('\n\n')


def compare(a, b):
    print(a)
    print("against")
    print(b)
    print()
    while True:
        if a:
            x = a.pop(0)
        else:
            return True
        if b:
            y = b.pop(0)
        else:
            return False

        if isinstance(x, int) and isinstance(y, int):
            if x < y:
                return True
            if x > y:
                return False

        elif isinstance(x, list) and isinstance(y, list):
            return compare(x, y)

        elif isinstance(x, int) and isinstance(y, list):
            return compare([x], y)

        elif isinstance(x, list) and isinstance(y, int):
            return compare(x, [y])
        else:
            assert False



add = 0
for i, block in enumerate(blocks):
    aa, bb = block.split("\n")
    aa = eval(aa)
    bb = eval(bb)
    print("---")
    if compare(aa, bb):
        add += (i + 1)
        print("TRUE!")
    else:
        print("FALSE!")
    print("---")
    print()
print()
print(add)
