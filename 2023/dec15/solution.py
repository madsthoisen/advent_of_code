from collections import defaultdict


with open("input") as f:
    ins = f.read().strip().split(',')


def get(s):
    curr = 0
    for x in s:
        curr += ord(x)
        curr *= 17
        curr %= 256
    return curr


# part I
print(sum(get(s) for s in ins))

# part II
boxes = defaultdict(list)
for x in ins:
    if '-' in x:
        label = x[:-1]
        box = get(label)
        boxes[box] = [x for x in boxes[box] if x[0] != label]
    elif '=' in x:
        label, fl = x.split('=')
        box = get(label)
        new_boxes = defaultdict(list)
        not_present = True
        for d in boxes:
            for (a, b) in boxes[d]:
                if a != label:
                    new_boxes[d].append((a, b))
                elif a == label:
                    new_boxes[d].append((a, int(fl)))
                    not_present = False
        boxes = new_boxes
        if not_present:
            boxes[box].append((label, int(fl)))

print(sum((k + 1) * (i + 1) * b for k in range(256) for i, (_, b) in enumerate(boxes[k])))
