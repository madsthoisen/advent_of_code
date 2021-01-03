import re

with open("input") as f:
    ips = [line.strip() for line in f.readlines()]

def abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i] != s[i + 1] == s[i + 2]:
            return True
    return False

def tls(ip):
    pat = r"\[\w*\]"
    for br in re.findall(pat, ip):
        if abba(br[1:-1]):
            return False
    for part in re.split(pat, ip):
        if abba(part):
            return True
    return False

def abas(s):
    S = set()
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] != s[i + 1]:
            S.add(s[i:i + 3])
    return S

def ssl(ip):
    pat = r"\[\w*\]"
    abas_set = set()
    for part in re.split(pat, ip):
        abas_set = abas_set.union(abas(part))
    for br in re.findall(pat, ip):
        for aba in abas_set:
            if aba[1] + aba[0] + aba[1] in br:
                return True
    return False

# part I
print(sum(map(tls, ips)))

# part II
print(sum(map(ssl, ips)))
