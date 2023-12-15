from functools import reduce


with open("input") as f:
    ins = f.read().strip().split(',')


def get(s):
    return reduce(lambda x, y: (x + ord(y)) * 17 % 256, s, 0)


# part I
print(sum(get(s) for s in ins))

# part II
boxes = {i: dict() for i in range(256)}
for x in ins:
    if '-' in x:
        label = x[:-1]
        box = get(label)
        boxes[box].pop(label, None)
    elif '=' in x:
        label, fl = x.split('=')
        box = get(label)
        boxes[box][label] = int(fl)
        for b in set(boxes) - {box}:
            boxes[b].pop(label, None)

print(sum((k + 1) * (i + 1) * b for k, box in boxes.items() for i, (_, b) in enumerate(box.items())))
