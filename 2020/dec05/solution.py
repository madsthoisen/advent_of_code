with open("input") as f:
    tmp = [el.strip() for el in f.readlines()]
    seats = [(s[:7], s[7:]) for s in tmp]

def bin(chars, l, h, low, high):
    for c in chars:
        inc = (h - l + 1) // 2
        if c == high:
            l += inc
        elif c == low:
            h -= inc
    return l, h

def find_seat(seats):
    L = sorted(seats)
    for s in range(L[0], L[-1] + 1):
        if not s in seats:
            if {s - 1, s + 1}.issubset(seats):
                return s
    return False


seat_nos = set(bin(chars[0], 0, 127, "F", "B")[0] * 8
        + bin(chars[1], 0, 7, "L", "R")[0] for chars in seats)

print(max(seat_nos))
print(find_seat(seat_nos))
