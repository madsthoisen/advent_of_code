from collections import defaultdict
from re import finditer

with open("input") as f:
    repl, w = f.read().split("\n\n")
    w = w.strip()

react = defaultdict(list)
react_r = defaultdict(list)
for r in repl.split('\n'):
    a, b = r.split(" => ")
    react[a].append(b)
    react_r[b].append(a)

def evolve(w, react):
    return {w[:r.start()] + b + w[r.end():] for a in react for b in react[a] 
        for r in finditer(a, w)}

# part I
M = evolve(w, react)
print(len(M))

# part II // Dissapointingly, this greedy approach works on the particular input
i = 0
while True:
    w = min(evolve(w, react_r), key=len)
    i += 1
    if w == 'e':
        print(i)
        break
