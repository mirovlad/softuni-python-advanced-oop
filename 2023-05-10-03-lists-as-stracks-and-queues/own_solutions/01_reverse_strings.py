from collections import deque

in_string = input()

in_stack = deque(in_string)

while in_stack:
    print(in_stack.pop(), end="")
