import networkx as nx


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]
    grid = {r + c * 1j: lines[r][c] for r in range(len(lines)) for c in range(len(lines[0]))}


def get_n_sides(fence, region):
    total = 4
    for inc in [-1j, 1j]:
        ab = sorted([z + inc for z in fence if z + inc in region], key=lambda z: (z.imag, z.real))
        total += sum(z2.real - z1.real > 1 or z1.imag != z2.imag for z1, z2 in zip(ab, ab[1:]))

    for inc in [-1, 1]:
        lr = sorted([z + inc for z in fence if z + inc in region], key=lambda z: (z.real, z.imag))
        total += sum(z2.imag - z1.imag > 1 or z1.real != z2.real for z1, z2 in zip(lr, lr[1:]))
    return total


DIRS = [-1, 1, -1j, 1j]
G = nx.Graph()
G.add_nodes_from(grid)
G.add_edges_from([(z, z + dz) for z, val in grid.items() for dz in DIRS if grid.get(z + dz) == val])

part1, part2 = 0, 0
for region in nx.connected_components(G):
    fence = [z + dz for z in region for dz in DIRS if grid.get(z + dz) != grid[list(region)[0]]]
    part1 += len(region) * len(fence)
    part2 += len(region) * get_n_sides(fence, region)


# part I
print(part1)

# part II
print(part2)
