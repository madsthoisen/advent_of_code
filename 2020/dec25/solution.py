with open("input") as f:
    keys = [int(l.strip()) for l in f.readlines()]

sub = 7
p = 20201227
n = 0
while True:
    if pow(sub, n, p) == keys[0]:
       loop_size = n
       break
    n += 1

print(pow(keys[1], loop_size, p))
