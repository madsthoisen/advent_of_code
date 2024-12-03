import re


with open("input") as f:
    instructions = f.read()


def execute(part2=False):
    do = True
    add = 0
    for ins in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", instructions):
        nums = re.findall(r"\d+", ins)
        if nums:
            add += (int(nums[0]) * int(nums[1])) * do
        elif part2:
            do = ins == "do()"
    return add


# part I
print(execute())


# part II
print(execute(True))
