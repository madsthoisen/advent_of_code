import re

with open("input") as f:
    strings = [s.strip() for s in f.readlines()]

# part I
vowels = '[aeiou]' 
twice = r'(\w)\1{1,}' 
ex = 'ab|cd|pq|xy' 

count = 0
for string in strings:
    c1 = (len(re.findall(vowels, string)) > 2)
    c2 = re.search(twice, string)
    c3 = re.search(ex, string)
    if (c1 and c2) and (not c3):
        count += 1
print(count)

# part II
twice = r'(\w{2}).*\1'
repeats = r'(\w)\w{1}\1'
count = 0
for string in strings:
    c1 = re.search(twice, string)
    c2 = re.search(repeats, string)
    if c1 and c2:
        count += 1
print(count)


