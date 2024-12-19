with open("input") as f:
    b1, b2 = f.read().split("\n\n")


patterns = b1.split(", ")
designs = b2.split("\n")


def count(x, dp={}):
    if x == '':
        return 1
    if x not in dp:
        dp[x] = sum(count(x[len(p):], dp) for p in patterns if x[:len(p)] == p)
    return dp[x]


print(sum(count(design) > 0 for design in designs))

# part II
print(sum(count(design) for design in designs))
