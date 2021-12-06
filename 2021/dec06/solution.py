from collections import defaultdict


with open("input") as f:
    numbers = list(map(int, f.read().strip().split(',')))


def new_day(dic):
    new_dic = defaultdict(int)
    for k, v in dic.items():
        if k == 0:
            new_dic[8] = v
            new_dic[6] += v
        else:
            new_dic[k - 1] += v
    return new_dic


fish = {i: numbers.count(i) for i in range(7)}
for i in range(256):
    fish = new_day(fish)
    if i == 79:
        # part I
        print(sum(fish.values()))

# part II
print(sum(fish.values()))

