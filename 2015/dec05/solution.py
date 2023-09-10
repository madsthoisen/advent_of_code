import re


with open("input") as f:
    strings = [line.strip() for line in f.readlines()]


def vowels(s): return len(re.findall(r"[aeiou]", s)) > 2
def repeated(s): return re.search(r"(.)\1", s) is not None
def illegal(s): return re.search(r"ab|cd|pq|xy", s) is not None
def pair_twice(s): return re.search(r"(.{2}).*\1", s) is not None
def repeat(s): return re.search(r"(.).\1", s) is not None


# part I
print(sum(vowels(s) and repeated(s) and not illegal(s) for s in strings))

# part I
print(sum(pair_twice(s) and repeat(s) for s in strings))
