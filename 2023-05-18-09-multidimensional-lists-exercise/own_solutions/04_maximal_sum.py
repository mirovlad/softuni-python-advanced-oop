SUB_DIM = (3, 3)

from math import inf

dim = [int(x) for x in input().split()]
mat = [[int(x) for x in input().split()] for _ in range(dim[0])]

found_sub = {
    'mat': None,
    'sum': -inf,
}

for r in range(dim[0] - SUB_DIM[0] + 1):
    for c in range(dim[1] - SUB_DIM[1] + 1):
        sub_mat = []
        sub_sum = 0
        for sub_r in range(SUB_DIM[0]):
            sub_row = mat[r + sub_r][c: c + SUB_DIM[1]]
            sub_sum += sum(sub_row)
            sub_mat.append(sub_row)
        if sub_sum > found_sub["sum"]:
            found_sub["sum"] = sub_sum
            found_sub["mat"] = sub_mat

print(f"Sum = {found_sub['sum']}")
[print(*row) for row in found_sub["mat"]]
