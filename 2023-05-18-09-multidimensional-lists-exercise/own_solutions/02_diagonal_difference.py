size = int(input())
primary_sum = 0
secondary_sum = 0
for idx in range(size):
    row = input().split()
    primary_sum += (int(row[idx]))
    secondary_sum += int(row[size-idx-1])

print(abs(primary_sum - secondary_sum))
