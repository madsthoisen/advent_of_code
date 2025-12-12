with open("input") as f:
    blocks = f.read().split("\n\n")

add = 0
for x in blocks[-1].split("\n"):
    s, ps = x.split(": ")
    h, w = map(int, s.split('x'))
    add += (h * w >= sum(map(int, ps.split())) * 9)
print(add)
