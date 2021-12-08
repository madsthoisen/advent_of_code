with open("input") as f:
    lines = [line.strip().split(' | ') for line in f.readlines()]


# part I
print(sum([len(output) in {2, 3, 4, 7} for _, outputs in lines for output in outputs.split()]))


# part II
def get_rules(patterns):
    # number of segments: displayed number
    fixed = {2: 1, 3: 7, 4: 4, 7: 8}

    # (length, segments in common with 4, segments in common with 1): display number
    chars = {(5, 3, 2): 3,
             (5, 3, 1): 5,
             (5, 2, 1): 2,
             (6, 3, 2): 0,
             (6, 3, 1): 6,
             (6, 4, 2): 9}

    dic = {}
    for pat in sorted(patterns, key=len):
        l = len(pat)
        if l in fixed:
            dic[fixed[l]] = pat
        else:
            dic[chars[(l, len(pat & dic[4]), len(pat & dic[1]))]] = pat
    return dic


out = 0
for patterns, values in lines:
    patterns = list(map(set, patterns.split()))
    values = list(map(set, values.split()))
    dic = get_rules(patterns)
    number = ''.join([str(k) for val in values for k, v in dic.items() if val == v])
    out += int(number)
print(out)
 
