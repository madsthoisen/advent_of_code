import re


def next_letter(char):
    return chr((ord(char) - 97 + 1) % 26 + 97)


def inc(s):
    new_s = ''
    while s:
        s, x = s[:-1], s[-1]
        new_s = next_letter(x) + new_s
        if new_s[0] != 'a':
            return s + new_s
    return 'b' + new_s


def has_inc(s):
    ll = [ord(char) for char in s]
    for a, b, c in zip(ll, ll[1:], ll[2:]):
        if a + 2 == b + 1 == c:
            return True
    return False


def has_iol(s):
    return 'i' in s or 'o' in s or 'l' in s


def has_pairs(s):
    return len(re.findall(r"(.)\1", s)) > 1


def next_pwd(pwd):
    while True:
        pwd = inc(pwd)
        if has_inc(pwd) and not has_iol(pwd) and has_pairs(pwd):
            return pwd


puzzle_input = "vzbxkghb"

# part I
pwd = next_pwd(puzzle_input)
print(pwd)

# part II
print(next_pwd(pwd))
