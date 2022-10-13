from time import time

with open("input") as f:
    L = list(map(int, f.readlines()))

num = 2020

def f1(L, num):
    for i, l in enumerate(L):
        if l > num:
            continue
        for m in L[i+1:]:
            if l + m == num:
                return l * m

def f1_rec(L, num):
    l = L[0]
    if l > num:
        return f(L[1:], num)
    for m in L[1:]:
        if l + m == num:
            return l * m
    return f1_rec(L[1:], num)

def f1_set(L, num):
    L_set = set(L)
    for l in L:
        if num - l in L_set:
            return l * (num - l)

def f2(L, num):
    for i, l in enumerate(L):
        if l > num:
            continue
        for j, m in enumerate(L[i+1:]):
            if l + m > num:
                continue
            for n in L[j+1:]:
                if l + m + n == num:
                    return l * m * n

t0 = time()
print("part 1: ", f1(L,num), " (time: %.6f ms)" %((time() - t0)*1000))

t1 = time()
print("part 2: ", f2(L,num), " (time: %.6f ms)" %((time() - t1)*1000))

t2 = time()
print("part 1, rec.: ", f1_rec(L,num), " (time: %.6f ms)" %((time() - t2)*1000))

t3 = time()
print("part 1, hash: ", f1_set(L,num), " (time: %.6f ms)" %((time() - t3)*1000))
