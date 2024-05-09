from functools import reduce

size = int(input())

mat = [[int(x) for x in input().split()] for _ in range(size)]
# print(f"mat #{mat}#")

primary_sum = reduce(lambda s, r: s + r[1][r[0]], enumerate(mat), 0)
print(primary_sum)
