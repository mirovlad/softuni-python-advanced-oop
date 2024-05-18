# This solutions assumes matrix is square,
# As the problem description seems to imply silently

dim = int(input())

mat = [[int(x) for x in input().split()] for _ in range(dim)]
# print(f"OK mat {mat}")

ops = {
    'Add': lambda a, b: a + b,
    'Subtract': lambda a, b: a - b,
}

while True:
    feed = input()
    if feed == "END":
        break

    op, args = feed.split(maxsplit=1)
    args = args.split()

    if len(args) != 3:
        print("?? Invalid input")  # Probably unexpected by Judge
        continue

    try:
        r, c = int(args[0]), int(args[1])
    except ValueError:
        print("?? Invalid input")  # Probably unexpected by Judge
        continue

    if -1 < r < dim and -1 < c < dim:
        pass
    else:
        print("Invalid coordinates")
        continue

    try:
        val = int(args[2])
    except ValueError:
        print("?? Invalid input")  # Probably unexpected by Judge
        continue

    if op not in ops:
        print("?? Invalid input")  # Probably unexpected by Judge
        continue

    mat[r][c] = ops[op](mat[r][c], val)

for row in mat:
    print(*row, sep=" ")
