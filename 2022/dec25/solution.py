with open("input") as f:
    strings = [line.strip() for line in f.readlines()]


conv = {'2': 2, '1': 1, '0': 0, '-': - 1, '=': -2}
vonc = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}


def snafu_to_dec(s):
    return sum(conv[x] * 5**i for i, x in enumerate(s[::-1]))


def dec_to_snafu(dec):
    s = ''
    while dec:
        rem = dec % 5
        s += vonc[rem]
        if rem > 2:
            dec += rem
        dec //= 5
    return s[::-1]


# part I
print(dec_to_snafu(sum(map(snafu_to_dec, strings))))