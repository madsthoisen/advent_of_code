from itertools import count, takewhile


DIRECTIONS = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}


with open("input") as f:
    lines, moves = [block.split('\n') for block in f.read().split("\n\n")]
    moves = ''.join(moves)


def setup(lines):
    grid = {(r, c): val if val not in {'@', 'O'} else '.' for r, row in enumerate(lines) for c, val in enumerate(row)}
    boxes = {(r, c) for r, row in enumerate(lines) for c, val in enumerate(row) if val == "O"}
    start = next((r, c) for r, row in enumerate(lines) for c, val in enumerate(row) if val == "@")
    return grid, boxes, start


def get_boxes_to_move(boxes, r, c, dr, dc, m, part):
    jump = 1 if part == 1 else 2
    inc = 1 if part == 2 and m == '<' else 0
    above_person = [0] if part == 1 else [0, -1]
    above_box = [0] if part == 1 else [-1, 0, 1]

    if m in {'<', '>'}:
        return set(takewhile(lambda x: x in boxes, ((r + i * dr, c + (i + inc) * dc) for i in count(1, jump))))

    boxes_move = set()
    check = [(r + dr, c + dc + ab) for ab in above_person]
    while check:
        _r, _c = check.pop()
        if (_r, _c) in boxes:
            boxes_move.add((_r, _c))
            for lr in above_box:
                check.append((_r + dr, _c + dc + lr))
    return boxes_move


def solve(grid, boxes, start, part):
    r, c = start
    for m in moves:
        dr, dc = DIRECTIONS[m]
        boxes_to_move = get_boxes_to_move(boxes, r, c, dr, dc, m, part=part)
        if boxes_to_move:
            incs = [0, 1] if part == 2 else [0]
            if all(grid[(br + dr, bc + dc + inc)] != '#' for br, bc in boxes_to_move for inc in incs):
                boxes = boxes - boxes_to_move | {(r + dr, c + dc) for r, c in boxes_to_move}
                r, c = r + dr, c + dc
        elif grid[(r + dr, c + dc)] != "#":
            r, c = r + dr, c + dc
    return sum(r * 100 + c for r, c in boxes)


# part I
grid, boxes, start = setup(lines)
print(solve(grid, boxes, start, part=1))


# part II
newlines = [''.join(2 * val if val == "#" else val + '.' for val in row) for row in lines]
grid, boxes, start = setup(newlines)
print(solve(grid, boxes, start, part=2))
