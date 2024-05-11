SUB_DIM  = (2, 2)

dim = [int(x) for x in input().split()]
mat = [input().split() for _ in range(dim[0])]
# print(f"OK mat {mat}")

matches_cnt = 0
for r in range(dim[0] - SUB_DIM[0] + 1):
    for c in range(dim[1] - SUB_DIM[1] + 1):
        char = mat[r][c]
        do_match = True
        sub_r = r - 1
        for _ in range(SUB_DIM[0]):
            sub_r += 1
            sub_c = c - 1
            for __ in range(SUB_DIM[1]):
                sub_c += 1
                if char != mat[sub_r][sub_c]:
                    do_match = False
                    break
            if not do_match:
                break
        if do_match:
            matches_cnt += 1

print(matches_cnt)
