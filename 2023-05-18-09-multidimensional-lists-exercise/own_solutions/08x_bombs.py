from functools import reduce

dim = int(input())
mat = [[int(x) for x in input().split()] for x in range(dim)]
hits = [tuple(int(y) for y in x.split(',')) for x in input().split()]
# print(f"OK hits {hits}")

for hit in hits:
    if mat[hit[0]][hit[1]] > 0:
        damage = mat[hit[0]][hit[1]]
        for r in range(max(hit[0] - 1, 0), min(hit[0] + 2, dim)):
            for c in range(max(hit[1] - 1, 0), min(hit[1] + 2, dim)):
                if mat[r][c] > 0:
                    mat[r][c] -= damage
        mat[hit[0]][hit[1]] = 0


alive_count = 0
alive_sum = 0
for row in mat:
    for v in row:
        if v > 0:
            alive_count += 1
            alive_sum += v

print(f"Alive cells: {alive_count}")
print(f"Sum: {alive_sum}")
[print(*row) for row in mat]
