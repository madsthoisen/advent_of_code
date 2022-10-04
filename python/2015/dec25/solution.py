import re

with open("input") as f:
    r, c = list(map(int, re.findall(r"\d+", f.read().strip())))

s = r + c - 2
n = (s**2 + s) // 2 + c
num = 20151125
for _ in range(n - 1):
    num = (num * 252533) % 33554393
print(num)
