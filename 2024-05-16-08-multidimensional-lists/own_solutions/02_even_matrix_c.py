size = int(input())

mat = []
for _ in range(size):
    mat.append([y for y in [int(x) for x in input().split(', ')] if y % 2 == 0])

print(mat)
