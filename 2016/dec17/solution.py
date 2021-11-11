from hashlib import md5


def md5_hash(s):
    return md5(s.encode('utf-8')).hexdigest()


passcode = "lpvhkcbi"
stack = [((0, 0), '')]
chars_open = {'b', 'c', 'd', 'e', 'f'}
shortest_route, longest_route = 0, 0
while stack:
    new_stack = []
    while stack:
        (x, y), route = stack.pop()
        if not -1 < x < 4 or not -1 < y < 4:
            continue
        if (x, y) == (3, 3):
            if not shortest_route:
                shortest_route = route
            if len(route) > longest_route:
                longest_route = len(route)
            continue
        u, d, l, r = md5_hash(passcode + route)[:4]
        if u in chars_open:
            new_stack.append(((x, y - 1), route + 'U'))
        if d in chars_open:
            new_stack.append(((x, y + 1), route + 'D'))
        if l in chars_open:
            new_stack.append(((x - 1, y), route + 'L'))
        if r in chars_open:
            new_stack.append(((x + 1, y), route + 'R'))
    stack = new_stack

# part I
print(shortest_route)

# part II
print(longest_route)
