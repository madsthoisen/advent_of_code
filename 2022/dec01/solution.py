with open("input") as f:
     cals = sorted([sum(list(map(int, x.split('\n')))) for x in f.read().split('\n\n')])


# part I
print(cals[-1])

# part II
print(sum(cals[-3:]))
