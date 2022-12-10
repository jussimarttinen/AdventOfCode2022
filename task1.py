
with open("input1") as f:
    d = f.readlines()

L = [0]
for r in d:
    r = r.strip()
    if r != "":
        L[-1] = L[-1] + int(r)
    else:
        L.append(0)


L.sort()
print(L[-1])

print(sum(L[-3:]))