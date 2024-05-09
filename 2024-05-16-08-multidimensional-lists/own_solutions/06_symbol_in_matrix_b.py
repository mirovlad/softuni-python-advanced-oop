lines = [input() for _ in range(int(input()))]
symbol = input()
found_pos = None
for line_idx, line in enumerate(lines):
    for char_idx, c in enumerate(line):
        if c == symbol:
            found_pos = (line_idx, char_idx)
            break

    if found_pos:
        break

if found_pos:
    print(found_pos)
else:
    print(f"{symbol} does not occur in the matrix")
