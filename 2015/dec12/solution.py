import json


with open("input", "rb") as f:
    content = json.load(f)


def sum_things(t, ignore_red):
    if isinstance(t, str):
        return 0
    if isinstance(t, int):
        return t
    if isinstance(t, list):
        return sum(sum_things(x, ignore_red) for x in t)
    if isinstance(t, dict):
        if ignore_red and "red" in t.values():
            return 0
        return sum(sum_things(v, ignore_red) for v in t.values())


# part I
print(sum_things(content, False))

# part II
print(sum_things(content, True))
