import re

with open("input") as f:
    tmp = [re.split("\n| ", l.strip()) for l in f.read().split("\n\n")]
    passes = [{el.split(":")[0] : el.split(":")[1] for el in p} for p in tmp]

def valid(p):
    req_fields = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}
    return req_fields.issubset(set(p.keys()))

def valid2(p):
    if not valid(p):
        return False
    dig4 = re.compile(r"\d{4}")
    if not (dig4.search(p["byr"]) and (1920 <= int(p["byr"]) <= 2002)):
            return False
    if not (dig4.search(p["iyr"]) and (2010 <= int(p["iyr"]) <= 2020)):
            return False
    if not (dig4.search(p["eyr"]) and (2020 <= int(p["eyr"]) <= 2030)):
            return False
    match = re.match(r"(\d+)(cm|in)", p["hgt"])
    if not match:
        return False
    else:
        num, unit = int(match[1]), match[2]
        if (unit == "cm" and not (150 <= num <= 193)):
            return False
        if (unit == "in" and not (59 <= num <= 76)):
            return False
    if not re.search(r"#[0-9a-f]{6}", p["hcl"]):
        return False
    if not p["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    if not (re.search(r"\d{9}", p["pid"]) and len(p["pid"]) == 9):
        return False
    return True

print(sum(map(valid, passes)))
print(sum(map(valid2, passes)))
