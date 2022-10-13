from functools import reduce

def step(a):
    b = tuple((x + 1) % 2 for x in a[::-1])
    return a + (0,) + b


def get_check_sum(tup):
    same_tuples = {(0, 0), (1, 1)}
    check_sum = tuple(int(tup[i : i + 2] in same_tuples) for i in range(0, len(tup) - 1, 2))
    if len(check_sum) % 2:
        return check_sum
    else:
        return get_check_sum(check_sum)


def solve(input_str, disk_length):
    a = tuple(map(int, list(input_str)))
    while len(a) < disk_length:
        a = step(a)
    return ''.join((str(x) for x in get_check_sum(a[:disk_length])))


input_str = "10111011111001111"

# part I
print(solve(input_str, 272))

# part II
print(solve(input_str, 35651584))
