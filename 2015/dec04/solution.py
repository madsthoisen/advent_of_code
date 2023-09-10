from hashlib import md5
from itertools import count


def find(key, postfix):
    return next(i for i in count(0) if md5(bytearray(f"{key}{i}", "utf-8")).hexdigest().startswith(postfix))


key = "bgvyzdsv"

# part I
print(find(key, "00000"))

# part II
print(find(key, "000000"))
