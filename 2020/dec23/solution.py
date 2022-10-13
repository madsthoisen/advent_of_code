with open("input") as f:
    pos = list(map(int, f.read().strip()))


def rounds(N, pos):
    dic = {val: pos[(i + 1) % len(pos)] for i, val in enumerate(pos)}

    curr = pos[0]
    max_val = max(dic.values())
    for move in range(N):
        c1 = dic[curr]
        c2 = dic[c1]
        c3 = dic[c2]
        curr_next = dic[c3]

        dest = curr - 1
        while True:
            if dest not in {c1, c2, c3} and dest > 0:
                break
            if dest in {c1, c2, c3}:
                dest -= 1
            if dest < 1:
                dest = max_val

        dic[curr] = curr_next
        dic[c3] = dic[dest]
        dic[dest] = c1

        curr = curr_next

    out = str(dic[1])
    for _ in range(max_val - 2):
        out += str(dic[int(out[-1])])
    return out, dic[1] * dic[dic[1]]

# part I
part1, _ = rounds(100, pos)
print(part1)

# part II
pos += list(range(max(pos) + 1, 1_000_000 + 1))
_, part2 = rounds(10_000_000, pos)
print(part2)
