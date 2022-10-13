import numpy as np
from collections import defaultdict

with open("input") as f:
    rules, my_ticket, other_tickets = f.read().split("\n\n")
    my_ticket = list(map(int, my_ticket.split(':')[1].strip().split(',')))
    other_tickets = [list(map(int, l.split(','))) for l in other_tickets.split(':')[1].split('\n')[1:-1]]
    rules = [l.split(': ') for l in rules.split('\n')]
    rules = {r[0]: [list(map(int, el.split('-'))) for el in r[1].split(' or ')] for r in rules}

# part I
add = 0
valid_tickets = []
for ticket in other_tickets:
    ticket_val = []
    for field in ticket:
        field_val = any((r0[0] <= field <= r0[1] or r1[0] <= field <= r1[1]) for r0, r1 in rules.values())
        if field_val == False:
            add += field
        ticket_val.append(field_val)
    if all(ticket_val):
        valid_tickets.append(ticket)

print(add)

# part II
success = defaultdict(list)
for i in range(len(my_ticket)):
    field_values = [t[i] for t in valid_tickets]
    for key, (r0, r1) in rules.items():
        s = int(all(r0[0] <= f <= r0[1] or r1[0] <= f <= r1[1] for f in field_values))
        success[key].append(s)

fixed = set()
while True:
    for key, val in success.items():
        if key in fixed:
            continue
        if sum(val) == 1:
            for k, v in success.items():
                if k != key:
                    success[k] = [max(m - n, 0) for m, n in zip(success[k], success[key])]
            fixed.add(key)
    if sum(sum(m) for m in success.values()) == len(success.values()):
        break
print(np.prod([my_ticket[val.index(1)] for key, val in success.items() if key.startswith("departure")]))

