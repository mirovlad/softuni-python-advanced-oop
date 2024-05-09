size = tuple([int(x) for x in input().split(', ')])

sums = [0 for x in range(size[1])]
for _ in range(size[0]):
    for col_idx, col_value in enumerate(input().split()):
        sums[col_idx] += int(col_value)

print(*sums, sep="\n")
