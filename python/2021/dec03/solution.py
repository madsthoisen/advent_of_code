import numpy as np


with open("input") as f:
    binaries = np.array([np.array(list(map(int, line.strip()))) for line in f.readlines()])


def get_most_common(binaries):
    return [int(x >= len(binaries) / 2) for x in np.sum(binaries, axis=0)]


def binlist_to_int(l):
    return sum(x * 2**i for x, i in zip(l[::-1], range(len(l))))


def filter_bin(binaries, typ):
    binaries_ = binaries
    for i in range(len(binaries_[0])):
        target = get_most_common(binaries_)
        if typ == 1:
            target = [1 - x for x in target]
        binaries_ = [line for line in binaries_ if line[i] == target[i]]
        if len(binaries_) == 1:
            return binlist_to_int(binaries_[0])


# part I
most_common = get_most_common(binaries)
least_common = [1 - x for x in most_common]
gamma = binlist_to_int(most_common)
epsilon = binlist_to_int(least_common)
print(gamma * epsilon)


# part II
oxygen = filter_bin(binaries, 0)
co2 = filter_bin(binaries, 1)
print(co2 * oxygen)
