from collections import defaultdict
from itertools import count
from math import gcd


with open("input") as f:
    lines = [line.strip().split(" -> ") for line in f.readlines()]

flipflops = {}
conjunctions = {}
inputs = defaultdict(set)
for mod, destinations in lines:
    destinations = destinations.split(", ")
    prefix = mod[0]
    id = mod[1:]
    if prefix == "%":
        flipflops[id] = (False, destinations)
    elif prefix == "&":
        conjunctions[id] = ({}, destinations)
    else:
        broadcaster = destinations[:]
    for d in destinations:
        inputs[d].add(id)

conjunctions = {id: [{x: "l" for x in inputs[id]}, destinations] for id, (_, destinations) in conjunctions.items()}


def solve(flipflops, conjunctions, part2):
    sent_pulses = {"l": 0, "h": 0}
    numbers = set()
    for i in count(1):
        pulses = [("broadcaster", "l", "")]
        sent_pulses["l"] += 1
        while pulses:
            dest, level, sender = pulses.pop(0)
            if any(conjunctions["rm"][0][x] == "h" for x in ["dh", "qd", "bb", "dp"]):
                numbers.add(i)
                if len(numbers) == 4 and part2:
                    lcm = 1
                    for x in numbers:
                        lcm = lcm * x // gcd(lcm, x)
                    return lcm

            if dest == "broadcaster":
                for d in broadcaster:
                    pulses.append((d, level, dest))
                    sent_pulses[level] += 1

            elif dest in flipflops and level == "l":
                state, destinations = flipflops[dest]
                send_level = "l" if state else "h"
                flipflops[dest] = (not state, destinations)
                pulses.extend([(d, send_level, dest) for d in destinations])
                sent_pulses[send_level] += len(destinations)

            elif dest in conjunctions:
                memory, destinations = conjunctions[dest]
                conjunctions[dest][0][sender] = level
                criteria = all(v == "h" for v in memory.values())
                send_level = "l" if criteria else "h"
                pulses.extend([(d, send_level, dest) for d in destinations])
                sent_pulses[send_level] += len(destinations)

        if not part2 and i == 1000:
            return sent_pulses["l"] * sent_pulses["h"]


# part I
print(solve(dict(flipflops), dict(conjunctions), False))

# part II
print(solve(dict(flipflops), dict(conjunctions), True))
