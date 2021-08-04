from collections import defaultdict

with open("input") as f:
    instructions = [line.strip().split(' ') for line in f.readlines()]

bots = defaultdict(list)
for ins in instructions:
    if ins[0] == "value":
        bots[ins[5]].append(int(ins[1]))
        bots[ins[5]].sort()

output = defaultdict(list)
i = 0
while True:
    i += 1
    if i == 10000:
        break
    for ins in instructions:
        if ins[0] == "bot":
            b = ins[1]
            if len(bots[b]) != 2:
                continue
            l, h = ins[6], ins[11]
            low, high = bots[b].pop(0), bots[b].pop(-1)
            if (low, high) == (17, 61):
                part1 = b
            if ins[5] == "bot":
                bots[l].append(low)
                bots[l].sort()
            elif ins[5] == "output":
                output[l].append(low)
            if ins[10] == "bot":
                bots[h].append(high)
                bots[h].sort()
            elif ins[10] == "output":
                output[h].append(high)

# part I
print(part1)

# part II
print(output['0'][0] * output['1'][0] * output['2'][0])
