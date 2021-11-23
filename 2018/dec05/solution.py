import re
from string import ascii_lowercase, ascii_uppercase


with open("input") as f:
    polymer = f.read().strip()


lower_upper = [char + char.upper() for char in ascii_lowercase]
upper_lower = [char + char.lower() for char in ascii_uppercase]
reactions = lower_upper + upper_lower

def fully_react(polymer):   
    l = len(polymer) + 1
    while len(polymer) != l:
        l = len(polymer)
        for reaction in reactions:
            polymer = re.sub(reaction, '', polymer)
    return polymer


# part I
print(len(fully_react(polymer)))

# part II
shortest = len(polymer)
for lower, upper in zip(ascii_lowercase, ascii_uppercase):
    tmp_polymer = re.sub(upper, '', re.sub(lower, '', polymer))
    l = len(fully_react(tmp_polymer))
    shortest = min(l, shortest)
print(shortest)
