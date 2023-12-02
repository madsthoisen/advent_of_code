import re


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


def get(d):
    add = 0
    for x in lines:
        matches = re.finditer(rf"(?=({'|'.join(k for k in d)}))", x)
        digs = [match.group(1) for match in matches]
        add += int(str(d[digs[0]]) + str(d[digs[-1]]))
    return add


letters = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
digits = {str(i): i for i in range(1, 10)}

# part I
print(get(digits))

# part II
print(get(dict(**digits, **letters)))

