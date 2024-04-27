# !! Incorrect idea
# Not sure if it is completely useless :)

from collections import deque

in_expr = input()
# in_expr = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
open_idxs = deque()
close_idxs = deque()

for idx, char in enumerate(in_expr):
    if "(" == char:
        open_idxs.append(idx)
    elif ")" == char:
        close_idxs.append(idx)


while open_idxs and close_idxs:
    open_idx = open_idxs.pop()
    close_idx = close_idxs.popleft()
    if close_idx > open_idx:
        sub_expr = in_expr[open_idx:close_idx + 1:]
        print(sub_expr)
        continue

    print(f"?? Found closing parentheses at position {close_idx} before opening {open_idx}")

if open_idxs:
    print(f"?? Found unmatched opening parentheses at positions {open_idxs}")

if close_idxs:
    print(f"?? Found unmatched closing parentheses at positions {close_idxs}")




