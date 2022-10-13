import re


with open("input") as f:
	stream = f.read()

stream = re.sub(r'!.', '', stream)
length_before = len(stream)
garbage_pattern = r'<[^>]*>'
krokodillenaeb = len(re.findall(garbage_pattern, stream)) * 2
stream = re.sub(garbage_pattern, '', stream)

curr, add = 0, 0
for char in stream:
	if char == '{':
		curr += 1
		add += curr
	if char == '}':
		curr -= 1

# part I
print(add)

# part II
print(length_before - len(stream) - krokodillenaeb)
