from collections import deque

commands = {
    "1": lambda c: c["stack"].append(int(c["args"].popleft())),
    "2": lambda c: c["stack"].pop() if c["stack"] else None,
    "3": lambda c: print(max(c["stack"])) if c["stack"] else None,
    "4": lambda c: print(min(c["stack"])) if c["stack"] else None
}

stack = deque()

lines_num = int(input())

for _ in range(lines_num):
    inp = input()
    parts = deque(inp.split())
    if parts:
        cmd = parts.popleft()
        if cmd in commands:
            # print("before stack", stack)
            # print("inp", inp)
            commands[cmd]({  # context
                "stack": stack,
                "args": parts
            })
            # print("after stack", stack)
        else:
            print(f"?? Unsupported cmd {cmd}")
    else:
        print(f"?? unsupported input {inp}")

stack.reverse()
print(", ".join([str(x) for x in stack]))


