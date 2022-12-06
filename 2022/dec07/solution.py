import networkx as nx
import re

from collections import defaultdict, Counter
from utils import *


with open("input") as f:
    numbers = [int(x) for x in f.readlines()]  # one number per line
    #numbers = [int(x) for x in f.read().split(',')]  # comma separated numbers

    #b1, b2 = f.read.split('\n\n')  # two blocks
    #strings = [line.strip() for line in f.readlines()]
    #lines = [list(map(int, re.findall("-?\d+", line))) for line in strings]  # nums in every line of above

print(numbers)




#dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#nx.all_simple_paths()
#lol = [[0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0]]
#print_lol(lol, mode='lit')
#print(binlist_to_int([1, 0, 0, 1]))
#l = [1, 1, 2, 3, 44, 4, 4, 4]
#d = Counter(l)
#max(d, key=d.get))