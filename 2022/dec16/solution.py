import networkx as nx

from functools import cache


with open("input") as f:
    strings = [line.strip().split(" ") for line in f.readlines()]


G = nx.DiGraph()
flows = {}
for x in strings:
    curr = x[1]
    rate = int(x[4][5:-1])
    for a in x[9:]:
        dest = a.replace(",", "")
        G.add_edge(curr, dest)
    if rate > 0:
        flows[curr] = rate

paths = {s: [(v, c) for v, c in d.items() if s != v] for s, d in nx.floyd_warshall(G).items()}


# part I
@cache
def search(t, pos, f):
    flows_set = set(f)
    if t == 0 or not f:
        return 0
    # move and open
    m = 0
    for d, c in paths[pos]:
        if d in flows_set and t > c + 1:
            m = max(m, search(t - c - 1, d, tuple(sorted(flows_set - {d}))) + flows[d] * (t - c - 1))
    return m


print(search(30, "AA", tuple(flows.keys())))

# part II
@cache
def search(ty, py, te, pe, f):
    flows_set = set(f)
    if (ty == 0 and te == 0) or not f:
        return 0

    # Available moves
    you = [(ty - cy - 1, dy) for dy, cy in paths[py] if dy in flows_set and ty > cy + 1]
    ele = [(te - ce - 1, de) for de, ce in paths[pe] if de in flows_set and te > ce + 1]

    m = 0
    if you and ele:
        for _ty, _py in you:
            for _te, _pe in ele:
                if _pe == _py:
                    continue
                new_flows = tuple(sorted(flows_set - {_py} - {_pe}))
                gain = flows[_py] * _ty + flows[_pe] * _te
                ((t1, p1), (t2, p2)) = sorted([(_ty, _py), (_te, _pe)])
                m = max(m, search(t1, p1, t2, p2, new_flows) + gain)

    elif you and not ele:
        for _ty, _py in you:
            new_flows = tuple(sorted(flows_set - {_py}))
            gain = flows[_py] * _ty
            ((t1, p1), (t2, p2)) = sorted([(_ty, _py), (te, pe)])
            m = max(m, search(t1, p1, t2, p2, new_flows) + gain)

    elif not you and ele:
        for _te, _pe in ele:
            new_flows = tuple(sorted(flows_set - {_pe}))
            gain = flows[_pe] * _te
            ((t1, p1), (t2, p2)) = sorted([(ty, py), (_te, _pe)])
            m = max(m, search(t1, p1, t2, p2, new_flows) + gain)

    return m


print(search(26, "AA", 26, "AA", tuple(sorted(flows.keys()))))
