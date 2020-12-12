with open("input") as f:
    jolts = sorted(list(map(int, f.readlines())))

# part I
diffs = [jolts[0]] + [jolts[i] - jolts[i-1] for i in range(1, len(jolts))]
print(diffs.count(1) * (1 + diffs.count(3)))

# part II
def n_ways(L, num, dic):
    if (tuple(L), num) in dic:
        return dic[(tuple(L), num)]
    if len(L) == 0 or L[0] - num > 3:
        return 1
    out = sum(n_ways(L[n + 1:], L[n], dic) if (L[n] - num) <= 3 else 0 for n in range(3) if len(L) > n)
    dic[(tuple(L),num)] = out
    return out

print(n_ways(jolts, 0, {}))


