from hashlib import md5

with open("input") as f:
    tmp = f.read().strip()

pwd1 = ''
pwd2 = {}
i = -1
while True:
    i += 1
    w = md5((tmp + str(i)).encode("utf-8")).hexdigest()
    if w[:5] != "00000":
        continue
    if len(pwd1) < 8:
        pwd1 += w[5]
    if w[5].isdigit():
        a = int(w[5])
        if a not in pwd2:
            pwd2[a] = w[6]
            if set(range(8)).issubset(set(pwd2.keys())):
                break

# part I
print(pwd1)

# part II
print(''.join(pwd2[i] for i in range(8)))
