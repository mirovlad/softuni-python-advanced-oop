from functools import reduce

size = int(input())

mat = [[int(x) for x in input().split()] for _ in range(size)]
# print(f"mat #{mat}#")

primary_sum = 0
for idx, row in enumerate(mat):
    primary_sum += row[idx]
print(primary_sum)
