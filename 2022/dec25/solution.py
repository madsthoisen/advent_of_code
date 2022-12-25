with open("input") as f:
    strings = [line.strip() for line in f.readlines()]


conv = {'2': 2, '1': 1, '0': 0, '-': - 1, '=': -2}
vonc = {2: '2', 1: '1', 0: '0', -1: '-', -2: '='}


def snafu_to_dec(s):
    return sum(conv[x] * 5**i for i, x in enumerate(s[::-1]))


def dec_to_snafu(num):
    max_pow = 0
    while 5**max_pow < num:
        max_pow += 1

    stack = [(num, '')]
    for p in range(max_pow, -1, -1):
        new_stack = []
        while stack:
            total, s = stack.pop()
            if abs(total) > 2 * 5**(p + 1):
                continue
            for factor in [-2, -1, 0, 1, 2]:
                val = factor * 5**p
                dig = vonc[factor]
                if total - val == 0:
                    return s + dig + '0' * p
                else:
                    new_stack.append((total - val, s + dig))
        stack = new_stack


# part I
print(dec_to_snafu(sum(map(snafu_to_dec, strings))))