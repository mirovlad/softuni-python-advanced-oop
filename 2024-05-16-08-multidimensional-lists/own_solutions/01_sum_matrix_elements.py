from functools import reduce

rows_cnt, cols_cnt = [int(x) for x in input().split(', ')]
mat = [[int(x) for x in input().split(', ')] for _ in range(rows_cnt)]
s = reduce(lambda a, b: a + sum(b), mat, 0)

print(s)
print(mat)
