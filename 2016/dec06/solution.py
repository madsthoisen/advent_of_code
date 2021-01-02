from collections import Counter

with open("input") as f:
    rows = [line.strip() for line in f.readlines()]
    cols = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0]))]

# part I
print(''.join(Counter(col).most_common(1)[0][0] for col in cols))

# part II
print(''.join(Counter(col).most_common()[-1][0] for col in cols))
