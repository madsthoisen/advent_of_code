import numpy as np
import re
import scipy.optimize


with open("input") as f:
    blocks = [block.split("\n") for block in f.read().split("\n\n")]


def solve_milp(a, b, p, ub=None):
    c = [3, 1]
    res = scipy.optimize.linprog(
        c=c, A_eq=np.column_stack([a, b]), b_eq=p, bounds=((0, ub), (0, ub)),
        integrality=[1, 1], method="highs", options={"presolve": False})
    if res.success:
        return int(np.dot(c, res.x))
    return 0


def solve_linalg(a, b, p):
    A = np.column_stack([a, b])
    pa, pb = map(round, np.linalg.solve(A, p))
    if all(np.matmul(A, [pa, pb]) == p):
        return 3 * pa + pb
    return 0


def solve_bin_search(a, b, p):
    end_y_0 = p[0] / b[0] * b[1]
    end_y_1 = a[1] + (p[0] - 1 * a[0]) / b[0] * b[1]
    increasing = (end_y_1 > end_y_0)

    min_pusha = 0
    max_pusha = int(max(p[0] / a[0], p[1] / a[1])) + 1
    while True:
        pusha = min_pusha + (max_pusha - min_pusha) // 2
        pushb = (p[0] - pusha * a[0]) / b[0]
        end_y = pusha * a[1] + pushb * b[1]
        if end_y == p[1]:
            if pushb.is_integer():
                return int(3 * pusha + pushb)
            return 0
        if min_pusha == max_pusha:
            return 0
        if (end_y > p[1] and increasing) or (end_y < p[1] and not increasing):
            max_pusha = pusha - 1 if max_pusha == pusha else pusha
        if (end_y > p[1] and not increasing) or (end_y < p[1] and increasing):
            min_pusha = pusha + 1 if min_pusha == pusha else pusha


def solve(inc, ub):
    res_bin_search = 0
    res_linalg = 0
    res_milp = 0
    for i, ll in enumerate(blocks):
        a = list(map(int, re.findall(r'\d+', ll[0])))
        b = list(map(int, re.findall(r'\d+', ll[1])))
        p = [x + inc for x in map(int, re.findall(r'\d+', ll[2]))]
        res_bin_search += solve_bin_search(a, b, p)
        res_linalg += solve_linalg(a, b, p)
        res_milp += solve_milp(a, b, p, ub)

    return res_bin_search, res_linalg, res_milp


# part I
print(solve(0, ub=100))

# part II
print(solve(10000000000000, ub=None))
