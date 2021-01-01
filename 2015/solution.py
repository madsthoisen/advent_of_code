import re

with open("input") as f:
    me = list(map(int, [re.search(r"\d+", line)[0] for line in f.readlines()]))
    print(me)
