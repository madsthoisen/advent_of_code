with open("input") as f:
    numbers = [int(x) for x in f.read().split()]


count = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1
print(count)


count = 0
for i in range(4, len(numbers) + 1):
    if sum(numbers[i - 3 : i]) > sum(numbers[i - 4 : i - 1]):
        count += 1
print(count)

