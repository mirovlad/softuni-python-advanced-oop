# popleft() and then thinking

from collections import deque

food_supply = int(input())
food_orders = deque([int(x) for x in input().split()])

if food_orders:
    print(max(food_orders))

while food_orders and food_supply:
    # popleft() and then thinking
    food_order = food_orders.popleft()
    if food_order > food_supply:
        food_orders.appendleft(food_order)
        break

    food_supply -= food_order

if food_orders:
    print(f"Orders left: {' '.join([str(x) for x in food_orders])}")
else:
    print("Orders complete")



