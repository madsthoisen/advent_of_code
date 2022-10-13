from hashlib import md5

with open("input") as f:
    tmp = f.read().strip()

def pre(n):
    app = 0
    while True:
        num = md5((tmp + str(app)).encode('utf-8')).hexdigest()
        if num[:n] == '0'*n:
            return app
        app += 1

# part I
print(pre(5))

# part II
print(pre(6))

