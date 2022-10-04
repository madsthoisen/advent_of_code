# This solution only works on input where algorithm[0] = '#' and algorithm[-1] = '.'

from collections import defaultdict


with open("input") as f:
    algo, image = f.read().strip().split("\n\n")


image = [line.strip() for line in image.strip().split()]

h, w = len(image), len(image[0])
im = defaultdict(lambda: '.')
for r in range(h):
    for c in range(w):
        im[(r, c)] = image[r][c]


adj = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
for n in range(1, 51):
    new_im = defaultdict(lambda: '.') if not n % 2 else defaultdict(lambda: '#')
    for row in range(-n, h + n):
        for col in range(-n, w + n):
            s = ''.join(im[(row + i, col + j)] for i, j in adj).replace('.', '0').replace('#', '1')
            new_im[(row, col)] = algo[int(s, 2)]
    im = new_im

    # part I
    if n == 2:
        print(sum(v == '#' for v in im.values()))

# part II
print(sum(v == '#' for v in im.values()))
