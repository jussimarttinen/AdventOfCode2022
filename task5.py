import math
import string

with open("input5") as f:
    d = f.readlines()

x = d[0]
stacks = [[] for i in range(len(x) // 4)]
while x != "\n":
    for i in range(len(x) // 4):
        k = x[4*i:4*i+4].strip(" []\n")
        if k in string.ascii_uppercase and k:
            stacks[i].append(k)

    d.pop(0)
    x = d[0]

d.pop(0)

for x in d:
    x = x.strip()
    p = x.split()
    # for i in range(int(p[1])):
        # stacks[int(p[5])-1].insert(0, stacks[int(p[3])-1].pop(0))

    stacks[int(p[5])-1] = stacks[int(p[3])-1][:int(p[1])] + stacks[int(p[5])-1]
    stacks[int(p[3])-1] = stacks[int(p[3])-1][int(p[1]):]

print("".join(list(map(lambda x: x[0], stacks))))