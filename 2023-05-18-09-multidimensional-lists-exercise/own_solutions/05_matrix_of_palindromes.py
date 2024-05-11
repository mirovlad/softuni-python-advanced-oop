dim = [int(x) for x in input().split()]

start_char = 'a'
start_char_ord = ord(start_char)
mat = []
r_char_ord = start_char_ord - 1
for r in range(dim[0]):
    # print(f"OK r #{r}#")
    r_char_ord += 1
    r_char = chr(r_char_ord)
    row = []
    c_char_ord = r_char_ord - 1
    for c in range(dim[1]):
        c_char_ord += 1
        c_char = chr(c_char_ord)
        row.append(r_char + c_char + r_char)
    # print(f"OK row #{row}#")
    mat.append(row)

[print(*row) for row in mat]



