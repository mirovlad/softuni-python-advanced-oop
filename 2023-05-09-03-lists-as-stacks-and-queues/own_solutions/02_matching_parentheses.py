from collections import deque

in_expr = input()
# in_expr = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
open_idxs = deque()
orphan_close_idxs = []

for idx, char in enumerate(in_expr):
    if "(" == char:
        open_idxs.append(idx)
        continue

    if ")" == char:
        close_idx = idx
        if open_idxs:
            open_idx = open_idxs.pop()
            sub_expr = in_expr[open_idx:close_idx + 1:]
            print(sub_expr)
        else:
            orphan_close_idxs.append(close_idx)

if open_idxs:
    print(f"?? Found unmatched opening parentheses at position(s) {open_idxs}")
if orphan_close_idxs:
    print(f"?? Found unmatched closing parentheses at position {close_idx}")




