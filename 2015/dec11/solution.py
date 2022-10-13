with open("input") as f:
    pwd = f.read().strip()


def next_letter(s):
    return chr((ord(s) + 1 - 97) % 26 + 97)

def increment(s):
    new_s = ''
    for i in range(1, len(s)):
        c = next_letter(s[-i])
        new_s += c
        if c != 'a':
            break
    return s[:-i] + new_s[::-1]

def has_straight(pwd):
    streak = 1
    prev = -1
    for c in pwd:
        if ord(c) == prev + 1:
            streak += 1
            if streak == 3:
                return True
        else:
            streak = 1
        prev = ord(c)
    return False

def has_two_pairs(pwd):
    n_pairs = 0
    i = 0
    prev = ''
    while True:
        if i >= len(pwd):
            return n_pairs > 1
        c = pwd[i]
        if c == prev:
            n_pairs += 1
            i += 2
            if i < len(pwd):
                prev = pwd[i - 1]
            continue
        prev = c
        i += 1

def is_valid(pwd):
    if 'i' in pwd or 'o' in pwd or 'l' in pwd:
        return False
    if not has_two_pairs(pwd):
        return False
    if not has_straight(pwd):
        return False
    return True


# part I and II
count = 0
while True:
    pwd = increment(pwd)
    if is_valid(pwd):
        print(pwd)
        count += 1
        if count == 2:
            break
