from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])

wasted = 0
# fuse = 0
while cups and bottles:
    # fuse += 1
    # if fuse > 15:
    #     print("?? Fuse reached")
    #     exit()
    cup = cups.popleft()
    # print("OK cup", cup)
    while bottles and cup > 0:
        bottle = bottles.pop()
        # print("OK bottle", bottle)
        cup -= bottle
        # print("OK cup after", cup)

    if cup <= 0:
        wasted += (0 - cup)
    else:
        cups.appendleft(cup)

if cups:
    print(f"Cups: {' '.join([str(x) for x in cups])}")
else:
    bottles.reverse()
    print(f"Bottles: {' ' .join([str(x) for x in bottles])}")

print(f"Wasted litters of water: {wasted}")
