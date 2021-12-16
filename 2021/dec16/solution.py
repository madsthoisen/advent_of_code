from numpy import prod


with open("input") as f:
    _num = [x for x in f.read().strip()]


def get(n):
    return ''.join(num.pop(0) for _ in range(n))


def build_tree(num):
    vers = int(get(3), 2)
    ID = int(get(3), 2)

    if ID == 4:
        packet = ""
        while True:
            tmp = get(5)
            prefix, bits = tmp[0], tmp[1:]
            packet += bits
            if prefix == '0':
                return (vers, ID, int(packet, 2))

    else: 
        length_type_id = get(1)
        if length_type_id == '0':  # len of total subpackes
            val = int(get(15), 2)
            l = len(num)
            packages = []
            while l - len(num) <  val:
                packages.append(build_tree(num))
            return (vers, ID, packages)

        elif length_type_id == '1':  # num of subpackages
            val = int(get(11), 2)
            packages = [build_tree(num) for _ in range(val)]
    return (vers, ID, packages)


num = list(''.join(bin(int(char, 16))[2:].zfill(4) for char in _num))
packages = build_tree(num)

# part I
def add_version_numbers(arr):
    vers, _, packages = arr
    if type(packages) == int:
        return vers
    return vers + sum(add_version_numbers(p) for p in packages)

print(add_version_numbers(packages))


# part II
def get_value(arr):
    _, ID, packages = arr
    if type(packages) == int:
        return packages

    values = [get_value(p) for p in packages]
    if ID == 0:
        return sum(values)
    if ID == 1:
        return prod(values)
    if ID == 2:
        return min(values)
    if ID == 3:
        return max(values)
    if ID == 5:
        return int(values[0] > values[1])
    if ID == 6:
        return int(values[0] < values[1])
    if ID == 7:
        return int(values[0] == values[1])

print(get_value(packages))

