# This solution uses more deque-s and less indexing
# than the in-class solution
from collections import deque
from functools import reduce
import operator

ops = {
    "+": lambda n1, n2: n1 + n2,
    "-": lambda n1, n2: n1 - n2,
    "*": lambda n1, n2: n1 * n2,
    "/": lambda n1, n2: n1 // n2,
    # "+": operator.add,
    # "-": operator.sub,
    # "*": operator.mul,
    # "/": operator.floordiv,
}

nodes = deque(input().split())
while nodes[-1] in ops:
    args = deque()
    op = None
    while nodes:
        node = nodes.popleft()
        if node in ops:
            op = node
            break

        args.append(int(node))

    # Lib reduce
    n1 = reduce(lambda n1, n2: ops[op](n1, n2), args)

    # "Own reduce"
    # n1 = args.popleft()
    # while args:
    #     n2 = args.popleft()
    #     n1 = ops[op](n1, n2)

    nodes.appendleft(n1)

print(nodes[-1])
