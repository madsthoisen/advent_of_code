# Very heavily inspired by Jonathan Paulson's solution as presented in
# https://youtu.be/WiNkRStebpQ


with open("input") as f:
    numbers = (n for n in map(int, f.read().split(' ')))


def build_tree():
    children, metadata = [], []
    n_children = next(numbers)
    n_metadata = next(numbers)
    for _ in range(n_children):
        children.append(build_tree())
    for _ in range(n_metadata):
        metadata.append(next(numbers))
    return children, metadata


def sum_metadata(children, metadata):
    add = sum(metadata)
    add += sum(sum_metadata(child, metadata) for child, metadata in children)
    return add


def get_value(children, metadata):
    if not children:
        return sum(metadata)
    add = 0
    for child in metadata:
        if 0 <= child - 1 <= len(children) - 1:
            c, m = children[child - 1]
            add += get_value(c, m)
    return add


children, metadata = build_tree()

# part I
print(sum_metadata(children, metadata))

# part II
print(get_value(children, metadata))
