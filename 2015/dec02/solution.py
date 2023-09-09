with open("input") as f:
    dim = [list(map(int, x.strip().split('x'))) for x in f.readlines()]


def paper(d):
    l, w, h = d
    return 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])


def ribbon(d):
    l, w, h = d
    return 2*(sum(d) - max(d)) + l*w*h


# part I
print(sum(map(paper, dim)))

# part II
print(sum(map(ribbon, dim)))
