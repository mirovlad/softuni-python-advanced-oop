size = int(input())

mat = []
for _ in range(size):
    mat.append(list(filter(lambda x: x % 2 == 0, [int(x) for x in input().split(', ')])))

print(mat)
