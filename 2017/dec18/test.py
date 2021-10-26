def f():
	while True:
		x = yield
		yield x

tmp = f()
a = next(tmp)
print(a)
b = tmp.send(5)
print(b)
next(tmp)
c = tmp.send(6)
d = next(tmp)
print(c)
print(d)
