with open("input") as f:
    lines = [line.strip() for line in f.readlines()]


k = [[0, 0] for _ in range(10)]
tales = set()
tales.add(tuple(k[9]))
for l in lines:
    a, b = l.split(' ')
    b = int(b)
    print()
    print(l)
    for _ in range(b):
        if a == 'L':
            k[0][0] -= 1
        elif a == 'R':
            k[0][0] += 1
        if a == 'U':
            k[0][1] += 1
        elif a == 'D':
            k[0][1] -= 1
        for i in range(1, 10):
            t = k[i]
            h = k[i - 1]
            if h[1] - t[1] > 1 and h[0] - t[0] == 0:
                t[1] += 1
            if h[1] - t[1] < -1 and h[0] - t[0] == 0:
                t[1] -= 1
            if h[0] - t[0] > 1 and h[1] - t[1] == 0:
                t[0] += 1
            if h[0] - t[0] < -1 and h[1] - t[1] == 0:
                t[0] -= 1

            if abs(h[0] - t[0]) > 0 and abs(h[1] - t[1]) > 1:
                if h[1] > t[1]:
                    t[1] += 1
                if h[1] < t[1]:
                    t[1] -= 1
                if h[0] > t[0]:
                    t[0] += 1
                elif h[0] < t[0]:
                    t[0] -= 1

            if abs(h[1] - t[1]) > 0 and abs(h[0] - t[0]) > 1:
                if h[0] > t[0]:
                    t[0] += 1
                if h[0] < t[0]:
                    t[0] -= 1
                if h[1] > t[1]:
                    t[1] += 1
                elif h[1] < t[1]:
                    t[1] -= 1
        tales.add(tuple(k[9]))
        print(k)
print(len(tales))
print(tales)
# 6911 too high