import re

from collections import defaultdict
from datetime import datetime, timedelta


with open("input") as f:
    observations = sorted([line.strip() for line in f.readlines()])

sleeps = {}
for obs in observations:
    timestamp = datetime.strptime(re.findall(r'\[.*\]', obs)[0][1:-1], '%Y-%m-%d %H:%M')
    guard_no = re.findall(r'#[0-9]+', obs)
    if guard_no:
        guard = guard_no[0]
        if guard not in sleeps:
            sleeps[guard] = defaultdict(int)
    if re.search(r'asleep', obs):
        start = timestamp
    if re.search(r'wakes', obs):
        while start <= timestamp:
            sleeps[guard][start.minute] += 1
            start += timedelta(minutes=1)

# part I
guard = max([(sum(sleep.values()), guard) for guard, sleep in sleeps.items()])[1]
print(max(sleeps[guard], key=sleeps[guard].get) * int(guard[1:]))

## part II
max_sleep = 0
for guard, guard_sleep in sleeps.items():
    if len(guard_sleep):
        sleep = max(guard_sleep.values())
        if sleep > max_sleep:
            max_sleep = sleep
            part_2 = max(guard_sleep, key=guard_sleep.get) * int(guard[1:])

print(part_2)
