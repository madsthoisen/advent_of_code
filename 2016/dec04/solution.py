import re

from collections import Counter

with open("input") as f:
    rooms = [line.strip() for line in f.readlines()]

add = 0
for room in rooms:
    no = int(re.search(r"\d+", room)[0])
    check = room[-6 : -1]
    string = room[:-11]
    if "pole" in " ".join([''.join([chr((ord(w) - 97 + no) % 26 + 97)
                            for w in word])
                            for word in string.split('-')]):
        part2 = no
    count = Counter(sorted(string.replace('-', '')))
    if check == ''.join([el[0] for el in count.most_common(5)]):
        add += no

# part I
print(add)

# part II
print(part2)
