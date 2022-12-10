import re
import string


cd = re.compile(r"^\$ cd ([A-z]+)$")
ls = re.compile(r"\$ ls")
fl = re.compile(r"^(\d+) \w+\.?\w*$")
dr = re.compile(r"dir (\w+)")

with open("input7") as f:
    d = [l.strip() for l in f.readlines()]

dir_sizes = {"": 0}
current_dir = ""
for x in d:
    if x == "$ cd /": 
        current_dir = ""
    elif x == "$ cd ..":
        current_dir = current_dir[:current_dir.rfind("/")]
    else:
        k = re.match(cd, x)
        if k and k[1]:
            current_dir = current_dir + "/" + str(k[1])
            dir_sizes.setdefault(current_dir, 0)

    l = re.match(fl, x)
    if l:
        a = current_dir
        dir_sizes[a] += int(l[1])
        for i in range(current_dir.count("/")):
            a = a[:a.rfind("/")]
            dir_sizes[a] += int(l[1])


s = 0
for v in dir_sizes.values():
    if v <= 100000:
        s += v

v = dir_sizes[""] - 40000000


m = list(filter(lambda x: x >= v, dir_sizes.values()))


print(s)
print(min(m))