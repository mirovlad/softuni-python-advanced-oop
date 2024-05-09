size = tuple([int(n) for n in input().split(", ")])

matrix = [[int(n) for n in input().split(", ")] for _ in range(size[0])]

matrix_sum = sum([sum(r) for r in matrix])

print(matrix_sum)
print(matrix)
