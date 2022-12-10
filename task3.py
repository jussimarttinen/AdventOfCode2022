import string

with open("input3") as f:
    d = f.readlines()

k = 0
for s in d:
    s = s.strip()
    n = len(s) // 2 
    a, b = set(s[:n]), set(s[n:])

    for i in a.intersection(b):
        if i in string.ascii_lowercase:
            k += ord(i) - ord("a") + 1
        else:
            k += ord(i) - ord("A") + 27

print(k)
k = 0
for i in range(len(d)//3):
    s = [set(r.strip()) for r in d[3*i: 3*i+3]]

    for i in s[0].intersection(s[1]).intersection(s[2]):
        if i in string.ascii_lowercase:
            k += ord(i) - ord("a") + 1
        else:
            k += ord(i) - ord("A") + 27

print(k)
    