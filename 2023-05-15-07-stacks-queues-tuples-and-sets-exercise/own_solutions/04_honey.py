import operator
from collections import deque

workers = deque(list(map(int, input().split())))
nectars = deque(list(map(int, input().split())))
# print(f"workers {workers} nectars {nectars}")
ops = deque(input().split())

honey_maker = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    # "/": operator.floordiv,
}

honey = 0
while workers and nectars:
    worker = workers.popleft()
    nectar = nectars.pop()
    if nectar < worker:
        # Put the worker back from where we took them
        workers.appendleft(worker)
        continue

    if not ops:
        # print("?? Unexpected by description")
        break

    op = ops.popleft()
    if op == "/" and nectar == 0:
        continue

    honey += abs(honey_maker[op](worker, nectar))

print(f"Total honey made: {honey}")

if workers:
    print("Bees left: ", end="")
    print(*workers, sep=", ")

if nectars:
    print("Nectar left: ", end="")
    print(*nectars, sep=", ")

