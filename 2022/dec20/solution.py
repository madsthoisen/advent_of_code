with open("input") as f:
    numbers = [int(x) for x in f.readlines()]


class X:
    def __init__(self, val, prev=None, post=None):
        self.val = val
        self.prev = prev
        self.post = post


def solve(key, rounds):
    zero = next(i for i, x in enumerate(numbers) if x == 0)
    ll = [X(val=num*key) for num in numbers]
    for a, b in zip(ll, ll[1:]):
        a.post = b
        b.prev = a
    ll[0].prev = ll[-1]
    ll[-1].post = ll[0]

    for r in range(rounds):
        for x in ll:
            # convert negative steps to positive and remove roundtrips
            n_steps = x.val % (len(ll) - 1)

            # link neighbors
            x.prev.post = x.post
            x.post.prev = x.prev

            # move n_steps right
            a, b = x.prev, x.post
            for _ in range(abs(n_steps)):
                a = a.post
                b = b.post

            # link with destination
            a.post, b.prev = x, x
            x.prev, x.post = a, b

    x = ll[zero]
    l = [x := x.post for _ in range(3000)]
    return sum([l[i - 1].val for i in [1000, 2000, 3000]])


# part I
print(solve(1, 1))

# part II
print(solve(811589153, 10))
