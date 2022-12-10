with open("input2") as f:
    d = f.readlines()

s = 0
D = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
for k in d:
    k = k.strip()
    a, b = k.split(" ")
    s += D[b]
    s += 3 * ((D[a] - 3*D[b]) == 0 or (D[b] >= D[a] and (D[b] - 3*D[a]) != 0)) # draw or win
    s += 3 * ((D[a] - 3*D[b]) == 0 or (D[b] > D[a] and (D[b] - 3*D[a]) != 0)) # win

print(s)


D = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 1, "Z": 2}

s = 0
for k in d:
    k = k.strip()
    a, b = k.split(" ")
    s += D[b] * 3
    s += (D[a] + (D[b] - 2)) % 3 + 1

print(s)