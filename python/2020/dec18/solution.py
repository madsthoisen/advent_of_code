import re

with open("input") as f:
    nums = [line.strip() for line in f.readlines()]

def return_parens(expr):
    bal = 0
    start = -1
    for i, char in enumerate(expr):
        if char == '(':
            bal += 1
            if start == -1:
                start = i
        if char == ')':
            bal -= 1
            if bal == 0:
                return True, expr[start:i + 1]
    return False, None

def eval_part1(expr):
    while True:
        calc = re.findall(r'\d+ [\+\*] \d+', expr)
        if len(calc) == 0:
            return expr
        expr = expr.replace(calc[0], str(eval(calc[0])), 1)
    return expr

def eval_part2(expr):
    while True:
        a = re.findall(r'\d+ [\+] \d+', expr)
        if len(a) == 0:
           break
        expr = expr.replace(a[0], str(eval(a[0])), 1)
    while True:
        m = re.findall(r'\d+ [\*] \d+', expr)
        if len(m) == 0:
            return expr
        expr = expr.replace(m[0], str(eval(m[0])), 1)

def eval_aoc(expr, eval_fct):
    status = True
    while status:
        status, out = return_parens(expr)
        if status:
            expr = expr.replace(out, eval_aoc(out[1:-1], eval_fct))
    expr = eval_fct(expr)
    return expr


# part I
print(sum(map(int, map(lambda expr: eval_aoc(expr, eval_fct=eval_part1), nums))))

# part II
print(sum(map(int, map(lambda expr: eval_aoc(expr, eval_fct=eval_part2), nums))))
