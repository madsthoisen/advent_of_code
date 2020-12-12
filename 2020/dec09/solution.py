with open("input") as f:
    nums = [int(line.strip()) for line in f.readlines()]

def is_sum(num, s):
    for i, x in enumerate(s):
        if num - x in s[i+1:]:
            return True
    return False

def first_fail(nums):
    for i in range(25, len(nums) - 25):
        num = nums[i+25]
        if not is_sum(num, nums[i:i + 25]):
            return num
    return True

def cont(num, nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            L = nums[i:j]
            add = sum(L)
            if add > num:
                break
            if add == num:
                return min(L) + max(L)
# part I
print(num := first_fail(nums))

# part II
print(cont(num, nums))
