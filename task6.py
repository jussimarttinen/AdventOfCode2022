
with open("input6") as f:
    s = f.read()

# s="mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def f(s, l):
    for i in range(len(s)-l):
        if len(set(s[i:i+l])) == l:
            return i+l

print(f(s,4))
print(f(s,14))

