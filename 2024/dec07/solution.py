with open("input") as f:
    lines = [line.strip().split(': ') for line in f.readlines()]
    lines = [(int(a), list(map(int, b.split(' ')))) for a, b in lines]


def test(control, nums, concat):
    def con(x, y): return [int(str(x) + str(y))] if concat else []
    vals = {nums[0]}
    for b in nums[1:]:
        vals = {y for a in vals for y in [a + b, a * b] + con(a, b)}
    return any(x == control for x in vals)


# Part I
print(sum(c for c, n in lines if test(c, n, False)))

# Part II
print(sum(c for c, n in lines if test(c, n, True)))
