from collections import defaultdict


with open("input") as f:
    numbers = list(map(int, f.read().strip().split(',')))


fish = [numbers.count(i) for i in range(9)]
sizes = {}
for i in range(256):
    birth = fish.pop(0)
    fish[6] += birth
    fish.append(birth)
    sizes[i + 1] = sum(fish)

# part I
print(sizes[80])

# part II
print(sizes[256])
