sizes = tuple([int(n) for n in input().split(", ")])

m = [[int(n) for n in input().split(" ")] for _ in range(sizes[0])]

for c in range (sizes[1]):
    print(sum([m[r][c] for r in range(sizes[0])]))
