with open("input") as f:
    row = f.read().strip()


def grow(row):
    new_row = ''
    for i in range(len(row)):
        if i == 0:
            pos = '.' + row[:2]
        elif i == len(row) - 1:
            pos = row[-2:] + '.'
        else:
            pos = row[i - 1: i + 2]
        if pos in {'^^.', '.^^', '^..', '..^'}:
            new_row += '^'
        else:
            new_row += '.'
    return new_row


def solve(row, n_rows):
    count = row.count('.')
    for _ in range(n_rows):
        row = grow(row)
        count += row.count('.')
    return count

# part I
print(solve(row, 39))

# part II
print(solve(row, 399999))
