with open("input") as f:
    tmp = [line.strip().split('(') for line in f.readlines()]
    tmp = [(f.split(' ')[:-1], a[9:-1].split(', ')) for f, a in tmp]

allergens = {}
for food_list, al_list in tmp:
    for al in al_list:
        if al in allergens.keys():
            allergens[al] = set(allergens[al]).intersection(set(food_list))
        else:
            allergens[al] = set(food_list)

# part I
dirty = set([food for v in allergens.values() for food in v])

print(sum(1 for food_list, _ in tmp for food in food_list if food not in dirty))

# part II
determined = set()
while True:
    for food, pos_alls in allergens.items():
        if len(pos_alls) == 1:
            determined = determined.union(pos_alls)
        if len(pos_alls) > 1:
            allergens[food] = pos_alls - determined
    if sum(len(f) for f in allergens.values()) == len(allergens.values()):
        break

print(','.join([list(allergens[food])[0] for food in sorted(allergens)]))
