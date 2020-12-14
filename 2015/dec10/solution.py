import itertools as it

with open("input") as f:
    tmp = f.read().strip()

def look_and_say(nums):
    return ''.join([str(len(list(group))) + str(num) for num, group in it.groupby(nums)])

# part I
for _ in range(40):
    tmp = look_and_say(tmp)
print(len(tmp))

# part II
for _ in range(10):
   tmp = look_and_say(tmp)
print(len(tmp))
