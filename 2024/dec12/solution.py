import networkx as nx


with open("input") as f:
    lines = [line.strip() for line in f.readlines()]
    grid = {r + c * 1j: lines[r][c] for r in range(len(lines)) for c in range(len(lines[0]))}


DIRS = [-1, 1, -1j, 1j]
G = nx.Graph()
G.add_nodes_from(grid)
G.add_edges_from([(z, z + dz) for z, val in grid.items() for dz in DIRS if grid.get(z + dz) == val])

part1, part2 = 0, 0
for region in nx.connected_components(G):
    fence = [(z, z + dz) for z in region for dz in DIRS if grid.get(z + dz) != grid[list(region)[0]]]
    part1 += len(region) * len(fence)
    # remove pieces of fence where there is another piece below or to the right
    remove = {(z, nz) for z, nz in fence for dz in [1j, 1] if (z + dz, nz + dz) in fence}
    part2 += len(region) * len(set(fence) - remove)


# part I
print(part1)

# part II
print(part2)
