with open("input") as f:
    masses = list(map(int, f.readlines()))


def fuel(mass):
    return mass // 3 - 2

def fuel_fuel(mass):
    f = 0
    while True:
        mass = fuel(mass)
        if mass <= 0:
            return f
        f += mass


# part I
print(sum(fuel(mass) for mass in masses))

# part II
print(sum(fuel_fuel(mass) for mass in masses))
