# Intentionally solved without deque but with index arithmetics

dim = tuple([int(x) for x in input().split()])
snake = input()

snake_len = len(snake)
idx = -1
reverse = True
for _ in range(dim[0]):
    reverse = not reverse
    row = ""
    for c in range(dim[1]):
        idx += 1
        if idx >= snake_len:
            idx = 0
        row += snake[idx]
    if reverse:
        row = row[::-1]
    print(row)
