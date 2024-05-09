size = int(input())
mat = [list(input()) for _ in range(size)]
# print(f"mat {mat}")

term = input()

found = None
for r, row in enumerate(mat):
    for c, char in enumerate(row):
        if char == term:
            found = {
                "row": r,
                "col": c,
            }
            break
    if found:
        break

if found:
    print(f"({found['row']}, {found['col']})")
else:
    print(f"{term} does not occur in the matrix")

