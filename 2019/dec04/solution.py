import re


def non_decreasing(s):
    return sorted(s) == list(s)

def two(s):
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))

def two_not_three(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            if i != 0 and s[i - 1] == s[i]:
                continue
            elif i != len(s) - 2 and s[i + 1] == s[i + 2]:
                continue
            else:
                return True
    return False


l, h = 125730, 579381

# part I
print(sum(non_decreasing(str(pwd)) and two(str(pwd)) for pwd in range(l, h + 1)))

# part I
print(sum(non_decreasing(str(pwd)) and two_not_three(str(pwd)) for pwd in range(l, h + 1)))

