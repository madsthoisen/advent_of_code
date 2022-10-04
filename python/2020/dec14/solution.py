import itertools as it

with open("input") as f:
    tmp = [b.split("\n") for b in f.read().split("mask")]
    tmp = [[item.split(" = ") for item in b] for b in tmp]

ins = [([L[0][1]] + [[int(L[i][0][4:-1]), int(L[i][1])] for i in range(1,len(L) - 1)]) for L in tmp[1:]]

# part I
dic = {}
for L in ins:
    mask = L[0]
    for mem, val in L[1:]:
        val_bit = list("{0:b}".format(val).zfill(36))
        val_bit = ''.join([v if m == 'X' else m for v, m in zip(val_bit, mask)])
        dic[mem] = int(val_bit, 2)
print(sum(dic.values()))

# part II
dic = {}
for L in ins:
    mask = L[0]
    for mem, val in L[1:]:
        for comb in it.product("01", repeat = mask.count('X')):
            comb = list(comb)
            mem_bit = list("{0:b}".format(mem).zfill(36))
            mem_bit = [m if m == 1 else v for v, m in zip(mem_bit, mask)]
            mem_bit = [comb.pop(0) if m == 'X' else x for x, m in zip(mem_bit, mask)]
            dic[int(''.join(mem_bit), 2)] = val
print(sum(dic.values()))
