import numpy as np


with open("input") as f:
    lines = [list(map(int, line.strip())) for line in f.readlines()]


def get(binaries):
    half = len(binaries) / 2
    bit_sum = np.zeros(len(binaries[0]))
    for binary in binaries:
        bit_sum += np.array(list(binary))
    most_common = [int(x >= half) for x in bit_sum]
    least_common = [int(x < half) for x in bit_sum]
    return most_common, least_common


def list_to_bin(l):
    return int(''.join(str(x) for x in l), 2)


# part I
most_common, least_common = get(lines)
gamma = list_to_bin(most_common)
epsilon = list_to_bin(least_common)
print(gamma * epsilon)


# part II
lines_ = lines
for i in range(len(lines_[0])):
    most_common, _ = get(lines_)
    lines_ = [line for line in lines_ if line[i] == most_common[i]]
    if len(lines_) == 1:
        oxygen = list_to_bin(lines_[0])
        break

lines_ = lines
for i in range(len(lines[0])):
    _, least_common = get(lines_)
    lines_ = [line for line in lines_ if line[i] == least_common[i]]
    if len(lines_) == 1:
        co2 = list_to_bin(lines_[0])
        break

print(co2 * oxygen)
