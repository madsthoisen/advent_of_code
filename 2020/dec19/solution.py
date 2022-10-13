import re

with open("input") as f:
    rules, messages = f.read().split("\n\n")
    rules = dict([r.replace('\"', '').split(": ") for r in rules.split("\n")])
    messages = messages.split("\n")

def match(rule, m):
    if len(rule) == 0:
        if len(m) == 0:
            return True
        return False
    r = rule.pop(0)
    if r in {'a', 'b'}:
        mat = re.match(r, m)
        if mat:
            return match(rule, m[mat.end():])
        return False
    else:
        return any(match(r.split(' ') + rule, m) for r in rules[r].split(" | "))

# part I
print(sum(any(match(r.split(' '), message) for r in rules['0'].split(" | ")) for message in messages))

# part II
rules['8'] = "42 | 42 8"
rules['11'] = "42 31 | 42 11 31"
print(sum(any(match(r.split(' '), message) for r in rules['0'].split(" | ")) for message in messages))
