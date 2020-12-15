with open("input") as f:
    start = list(map(int, f.read().strip().split(',')))

def round(n, start):
    game = {num: i + 1 for i, num in enumerate(start[:-1])}
    say = start[-1]
    for r in range(len(start), n):
        num = say
        if num in game:
            say = r - game[num]
        else:
            say = 0
        game[num] = r
    return say

# part I
print(round(2020, start))

# part II
print(round(30000000, start))
