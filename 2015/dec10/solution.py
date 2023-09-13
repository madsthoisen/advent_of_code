import itertools as it


with open("input") as f:
    w = f.read().strip()


def look_and_say(nums):
    return ''.join(str(len(list(g))) + str(num) for num, g in it.groupby(nums))


# part I
for _ in range(40):
    w = look_and_say(w)
print(len(w))

# part II
for _ in range(10):
    w = look_and_say(w)
print(len(w))
