SUB_SIZE = (2, 2)

size = tuple([int(x) for x in input().split(', ')])
mat = [[int(x) for x in input().split(', ')] for _ in range(size[0])]
# print(f"OK size {size}")
# print(f"OK mat {mat}")

max_sum = None
nax_sum_sub_mat = None
for r in range(size[0] - SUB_SIZE[0] + 1):
    for c in range(size[1] - SUB_SIZE[1] + 1):
        sub_mat = []
        sub_sum = 0
        for sr in range(SUB_SIZE[0]):
            sub_row = mat[r + sr][c: c + SUB_SIZE[1]]
            sub_sum += sum(sub_row)
            sub_mat.append(sub_row)
        # print(f"OK r #{r}# c #{c}# sub_mat {sub_mat}")

        if max_sum is None or max_sum < sub_sum:
            max_sum = sub_sum
            nax_sum_sub_mat = sub_mat

if nax_sum_sub_mat:
    for row in nax_sum_sub_mat:
        print(*row, sep=" ")
    print(max_sum)




