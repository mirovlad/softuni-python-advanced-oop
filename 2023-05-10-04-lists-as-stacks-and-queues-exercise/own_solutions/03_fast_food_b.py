# First thinking and then popleft()

# https://judge.softuni.org/Contests/Compete/Index/1831#2
# Failed test https://judge.softuni.org/Contests/Submissions/View/33967228

from collections import deque

food = int(input())
# orders = deque(map(int, input().split()))
orders = deque([int(node) for node in input().split()])

print(max(orders))

while orders:
    # First thinking and then popleft()
    if orders[0] <= food:
        food -= orders.popleft()
    else:
        break

if orders:
    # print(f"Orders left: {' '.join(list(map(str, list(orders))))}")
    print(f"Orders left: {' '.join([str(order) for order in orders])}")
else:
    print("Orders complete")