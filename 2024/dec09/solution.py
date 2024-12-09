with open("input") as f:
    string = map(int, f.read().strip())


disc = []
blocks = []
free_blocks = []
id = 0
p = 0
for i, val in enumerate(string):
    if i % 2 == 0:
        disc += [id for _ in range(val)]
        blocks.append((id, val, p))
        id += 1
    elif i % 2 == 1:
        disc += [None for _ in range(val)]
        free_blocks.append((p,  val))
    p += val

size = len(disc)

# part I
_disc = [x for x in disc]
free = 0
for i, val in reversed(list(enumerate(disc))):
    if val is not None:
        while free < len(_disc):
            if _disc[free] is None:
                break
            free += 1
        if free < i:
            _disc[free] = val
            _disc[i] = None

print(sum(i * x for i, x in enumerate(_disc) if x))

# part II
while blocks:
    val, block_length, mem_idx = blocks.pop(-1)
    for i in range(len(free_blocks)):
        p, free_block_length = free_blocks[i]
        if free_block_length >= block_length and p < mem_idx:
            disc[p: p + block_length] = [val for _ in range(block_length)]
            disc[mem_idx: mem_idx + block_length] = [None for _ in range(block_length)]
            free_blocks[i] = (p + block_length, free_block_length - block_length)
            break

print(sum(i * x for i, x in enumerate(disc) if x))
