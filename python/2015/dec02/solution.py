with open("input") as f:
    tmp = [line.strip() for line in f.readlines()]
    gifts = [list(map(int, l.split('x'))) for l in tmp]

def paper(gift):
    l, w, h = gift 
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def ribbon(gift):
    l, w, h = gift 
    return l*w*h + 2*(l + w + h - max([l, w, h]))

# part I
print(sum(map(paper, gifts)))

# part II
print(sum(map(ribbon, gifts)))
