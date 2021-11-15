with open("input") as f:
    nodes_raw = [line.strip().split() for line in f.readlines()]


nodes = {}
for node in nodes_raw[2:]:
    pos = tuple([int(x[1:]) for x in node[0].split('-')[-2:]])
    nodes[pos] = [int(x[:-1]) for x in node[1:-1]]


# part I
nodes_list = list(nodes.keys())
viable_pairs = 0
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        n, m = nodes[nodes_list[i]], nodes[nodes_list[j]]
        if 0 < n[1] <= m[2] or 0 < m[1] < n[2]:
            viable_pairs += 1
        
print(viable_pairs)

# part II
empty_node = [key for key, val in nodes.items() if val[1] == 0][0]
print("Empty node:", empty_node)
for key, val in nodes.items():
    if val[1] >= nodes[empty_node][2]:
        print("barrier", key, val)

# Empty node is on (11, 22). Need to move this to (28, 0). 
# This takes 22 + 17 + 8 steps due to the "barrier" on depth 14. 
# Then swap with the goal data and then do 28 roundtrips around 
# the goal data and move it (5 moves)
print(22 + 17 + 8 + 1 + 28 * 5)
