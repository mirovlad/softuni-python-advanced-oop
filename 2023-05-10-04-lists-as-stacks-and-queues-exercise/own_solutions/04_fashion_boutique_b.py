clothes_stack = list(map(int, input().split()))
rack_capacity = int(input())

racks = []

rack = None
cloth = None
while True:
    if cloth is None:
        if clothes_stack:
            cloth = clothes_stack.pop()
        else:
            break

    if rack is None:
        rack = []
        racks.append(rack)

    if sum(rack) + cloth <= rack_capacity:
        rack.append(cloth)
        cloth = None
    else:
        rack = None

print(len(racks))

