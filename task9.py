class Rope:

    def __init__(self, n_parts):
        self.n = n_parts
        self.rope = [(0,0) for i in range(self.n)]
        self.visited = [(0,0)]

    def move_all(self, head_dir):
        self.rope[0] = self.move_head(head_dir)
        for i in range(self.n-1):
            self.rope[i+1] = self.move_part(self.rope[i], self.rope[i+1])
        if self.rope[-1] not in self.visited:
            self.visited.append(self.rope[-1])

    def move_head(self, head_dir):
        h = self.rope[0]
        if head_dir == "U":
            return (h[0], h[1] + 1)
        elif head_dir == "D":
            return (h[0], h[1] - 1)
        elif head_dir == "L":
            return (h[0]-1, h[1])
        else:
            return (h[0]+1, h[1])

    def move_part(self, parent_pos, child_pos):
        dx = parent_pos[0] - child_pos[0]
        dy = parent_pos[1] - child_pos[1]
        if max(abs(dx), abs(dy)) <= 1:
            return child_pos
        else:
            return (child_pos[0] + Rope.sign(dx), child_pos[1] + Rope.sign(dy))

    @staticmethod
    def sign(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0


# part 1 & 2
with open("input9") as f:
    d = [(a, int(b)) for a, b in  list(map(lambda x: x.strip().split(), f.readlines()))]

r = Rope(2)
r2 = Rope(10)
for a, b in d:
    for i in range(b):
        r.move_all(a)
        r2.move_all(a)

print(len(r.visited))
print(len(r2.visited))

