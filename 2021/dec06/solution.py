with open("input") as f:
    numbers = list(map(int, f.read().strip().split(',')))


fish = [numbers.count(i) for i in range(9)]
for i in range(256):
    fish.append(fish.pop(0))
    fish[6] += fish[8]
    if i + 1 == 80:
        # part I
        print(sum(fish))

# part II
print(sum(fish))
