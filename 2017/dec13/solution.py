from itertools import count


with open("input") as f:
    tmp = [line.strip().split(": ") for line in f.readlines()]
    firewall = {int(d): int(r) for d, r in tmp}


def get_severity(delay=0):
    return sum(
        depth * t
        for t in range(delay, delay + max(firewall.keys()) + 1)
        if (depth := firewall.get(t - delay)) and t % (2 * (depth - 1)) == 0
    )


# part I
print(get_severity(0))

# part II
for delay in count():
    if get_severity(delay) == 0:
        print(delay)
        break
