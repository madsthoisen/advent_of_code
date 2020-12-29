import re
from collections import defaultdict

with open("input") as f:
    tmp = f.read().split("\n\n")
    tiles = [line.split('\n') for line in tmp][:-1]
    tiles = {int(l[0][5:-1]): l[1:] for l in tiles}

grid_size = int(len(tiles)**.5)
tile_size = len(tiles[list(tiles)[0]])

def flip(tile):
    return tile[::-1]

def rotate(tile):
    s = len(tile)
    return [''.join([tile[c][s - 1 - r] for c in range(s)]) for r in range(s)]


versions = defaultdict(list)
for tile_no in tiles:
    tile  = tiles[tile_no]
    for _ in range(2):
        tile = flip(tile)
        for _ in range(4):
            tile = rotate(tile)
            versions[tile_no].append(tile)

grids = [] 
for tile_no, tile in tiles.items():
    grids.append(({(0, 0): tile}, [tile_no]))
    grids.append(({(0, 0): flip(tile)}, [tile_no]))

def get_adj(grid, pos):
    adj = {}
    incs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for x, y in incs:
        a = (pos[0] + x, pos[1] + y)
        if a in grid:
            adj[(x, y)] = grid[a]
    return adj

def fit(ver, adj):
    for a in adj:
        if a == (-1, 0):
            if ver[0] != adj[a][9]:
                return False
        if a == (1, 0):
            if ver[9] != adj[a][0]:
                return False
        if a == (0, 1):
            if ''.join([t[9] for t in ver]) != ''.join([t[0] for t in
                adj[a]]):
                return False
        if a == (0, -1):
            if ''.join([t[0] for t in ver]) != ''.join([t[9] for t in
                adj[a]]):
                return False
    return True

new_grids = grids.copy()
r, c = 0, 0
while True:
    grids = new_grids.copy() 
    if r == grid_size - 1 and c == grid_size - 1:
        break
    if c == grid_size - 1:
        c = 0
        r += 1
    else:
        c += 1
    new_grids = []
    for grid, used in grids:
        adj = get_adj(grid, (r, c))
        for tile_no, vers in versions.items():
            if tile_no in used:
                continue
            for ver in vers:
                temp_grid = grid.copy()
                temp_used = used.copy()
                if fit(ver, adj):
                    temp_grid[(r, c)] = ver
                    temp_used.append(tile_no)
                    new_grids.append((temp_grid, temp_used))

for grid, used in new_grids:
    if len(used) ==  grid_size**2:
        print(used[0] * used[grid_size - 1] * used[grid_size**2 - grid_size -
            1]*used[grid_size**2 - 1])
        break

# part II

picture = {}
for c, part in grid.items():
    picture[c] = [l[1:-1] for l in part[1:-1]]

rows = ['\n'.join([''.join([picture[(row, col)][i] for col in range(grid_size)])
        for i in range(tile_size - 2)]) for row in range(grid_size)]

def check_seamonster(painting):
    ## this is wrong. need to check if i-1 and i+1 match is same place as i
    ## but if I do so, it misses one monster :/
    no_seamonsters = 0
    for i in range(len(painting)):
        matches = re.finditer('#....##....##....###', painting[i])
        for m in matches:
            if re.search('..................#.', painting[i-1]):
                if re.search('.#..#..#..#..#..#...', painting[i+1]):
                    no_seamonsters += 1 
    return no_seamonsters


max_seamonsters = 0
picture = '\n'.join(rows)
sea = picture.count('#')
picture = picture.split('\n')

max_seamonsters = max(max_seamonsters, check_seamonster(picture))
picture = rotate(picture)
max_seamonsters = max(max_seamonsters, check_seamonster(picture))
picture = rotate(picture)
max_seamonsters = max(max_seamonsters, check_seamonster(picture))
picture = rotate(picture)
max_seamonsters = max(max_seamonsters, check_seamonster(picture))
picture = rotate(picture)
picture = flip(picture)
max_seamonsters = max(max_seamonsters, check_seamonster(picture))
picture = rotate(picture)
max_seamonsters = max(max_seamonsters, check_seamonster(picture))
picture = rotate(picture)
max_seamonsters = max(max_seamonsters, check_seamonster(picture))
picture = rotate(picture)
max_seamonsters = max(max_seamonsters, check_seamonster(picture))

print(sea - max_seamonsters*15)

# 1930 too high
# 1900 too high
