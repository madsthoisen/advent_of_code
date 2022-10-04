from sympy import divisors

with open("input") as f:
    number = int(f.read())

def part1():
    i = 0
    while True:
        if 10 * sum(divisors(i)) >= number:
            return i
        i += 1

def part2():
    m = number // 11
    presents = [0] * m 
    for elf in range(1, m):
        for a in range(1, 51):
            house = elf * a
            if house >= m:
                break
            presents[house] += elf * 11
    return next(i for i, p in enumerate(presents) if p >= number)

# part I
print(part1())

# part II
print(part2())
