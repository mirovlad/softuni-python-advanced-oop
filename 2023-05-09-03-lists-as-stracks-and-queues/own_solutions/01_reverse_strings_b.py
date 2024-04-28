in_string = input()

in_stack = list(in_string)

out_stack = []
while in_stack:
    out_stack.append(in_stack.pop())

out_string = "".join(out_stack)

print(out_string)