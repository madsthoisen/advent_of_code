with open("input") as f:
    s = f.read()


# part I
print(min(i for i in range(len(s)) if len(set(s[i - 4: i])) == 4))

# part II
print(min(i for i in range(len(s)) if len(set(s[i - 14: i])) == 14))