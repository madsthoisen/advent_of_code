import numpy as np


with open("input") as f:
    claims = [line.strip().split(" ") for line in f.readlines()]


size = 1000
fabric = np.zeros((size, size))
claim_dic = {}
for claim in claims:
    claim_no = int(claim[0][1:])
    x, y = list(map(int, claim[2][:-1].split(",")))
    w, h = list(map(int, claim[3].split("x")))
    fabric[y : y + h, x : x + w] += 1
    claim_dic[claim_no] = set(
        [(i, j) for j in range(y, y + h) for i in range(x, x + w)]
    )

# part I
print((fabric > 1).sum())

# part II
for i in range(1, claim_no + 1):
    if not sum(
        len(claim_dic[i].intersection(claim_dic[j]))
        for j in range(1, claim_no + 1)
        if j != i
    ):
        print(i)
        break
