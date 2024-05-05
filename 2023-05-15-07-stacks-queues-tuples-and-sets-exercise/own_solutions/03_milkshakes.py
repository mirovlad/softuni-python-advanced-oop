from collections import deque

SHAKES_NEEDED = 5
CHOCO_RM = 5

chocos = deque([int(x) for x in input().split(', ')])
milks = deque([int(x) for x in input().split(', ')])

shakes = 0
while chocos and milks and shakes < SHAKES_NEEDED:
    choco = chocos.pop()
    milk = milks.popleft()
    if choco <= 0 or milk <= 0:
        if choco > 0:
            chocos.append(choco)
        if milk > 0:
            milks.appendleft(milk)
        continue

    if choco == milk:
        shakes += 1
        continue

    milks.append(milk)
    chocos.append(choco - CHOCO_RM)

if shakes < SHAKES_NEEDED:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

print(f"Chocolate: {', '.join(map(str, chocos))}") if chocos else print("Chocolate: empty")

print(f"Milk: {', '.join(map(str, milks))}") if milks else print("Milk: empty")
