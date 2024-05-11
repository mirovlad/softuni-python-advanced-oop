# This solution is more intended to explore dispatcher and exceptions design

dim = tuple([int(x) for x in input().split()])
mat = [input().split() for _ in range(dim[0])]


class InvalidInput(Exception):
    pass


def op_swap(args):
    result = {"final": False, "success": True, "print": True}

    args_len = len(args)
    if len(args) != 4:
        raise InvalidInput(f"Swap arguments must be exactly 4 (received {args_len})")

    try:
        r1, c1, r2, c2 = [int(x) for x in args]
    except ValueError:
        raise InvalidInput(f"Swap arguments must be integers (received {args})")

    try:
        mat[r1][c1], mat[r2][c2] = mat[r2][c2], mat[r1][c1]
    except IndexError:
        raise InvalidInput(f"Index out of range (received {args} vs dim {dim})")

    result["success"] = True
    return result


def op_end(args):
    return {"final": True, "success": True, "print": False}


ops = {
    "swap": op_swap,
    "END": op_end,
}

while True:
    op, *args = input().split()
    # print(f"OK op {op} args {args}")
    try:
        if op in ops:
            result = ops[op](args)
            # print(f"OK result {result}")
            if result["print"]:
                [print(*row, sep=" ") for row in mat]
            if result["final"]:
                break
        else:
            raise InvalidInput(f"Operation #{op}# not found")
    except InvalidInput:
        print("Invalid input!")




