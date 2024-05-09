size = int(input())

primary_diagonal_sum = 0
for idx in range(size):
    primary_diagonal_sum += [int(n) for n in input().split()][idx]
print(primary_diagonal_sum)