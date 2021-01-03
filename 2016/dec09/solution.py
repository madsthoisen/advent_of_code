with open("input") as f:
    compressed = f.read().strip()

dp = {}
def count_chars(comp):
    if comp in dp:
        return dp[comp], 0

    i, count, p1 = 0, 0, 0
    while i < len(comp):
        if comp[i] != '(':
            count += 1
            p1 += 1
        else:
            tmp = ''
            i += 1
            while comp[i] != ')':
                tmp += comp[i]
                i += 1
            inc, rep = map(int, tmp.split('x'))
            count += count_chars(comp[i + 1 : i + 1 + inc] * rep)[0]
            p1 += inc * rep
            i += inc
        i += 1
    dp[comp] = count
    return count, p1


p2, p1 = count_chars(compressed)

# part I
print(p1)

# part II
print(p2)
