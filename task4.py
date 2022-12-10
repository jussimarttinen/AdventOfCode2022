with open("input4") as f:
    d = list(map(lambda x: x.strip(), f.readlines()))
    d = list(filter(lambda x: len(x), d))

s = 0
r = 0
for x in d:
    x = x.split(",")
    a = list(map(int, x[0].split("-")))
    b = list(map(int, x[1].split("-")))
    if (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1]):
        s += 1
    if (a[0] <= b[1] <= a[1]) or (b[0] <= a[1] <= b[1]):
        r += 1

print(s)
print(r)
 