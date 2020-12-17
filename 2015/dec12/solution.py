import json

with open("input", "rb") as f:
    content = json.load(f)

def sum_elems(elem, add, ignore_red):
    if isinstance(elem, str):
        return 0
    if isinstance(elem, int):
        return elem
    if isinstance(elem, list):
        return sum(sum_elems(el, add, ignore_red) for el in elem)
    if isinstance(elem, dict):
        if ignore_red:
            if "red" in elem.keys() or "red" in elem.values():
                return 0
        return add + sum([sum_elems(val, add, ignore_red) for key, val in elem.items()])

# part I
print(sum_elems(content, 0, False))

# part II
print(sum_elems(content, 0, True))
