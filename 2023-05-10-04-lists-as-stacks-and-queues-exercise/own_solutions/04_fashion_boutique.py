from collections import deque

box_clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())

racks = []
rack = []
while box_clothes:
    cloth = box_clothes.pop()
    if cloth > rack_capacity:
        print(f"?? Ignoring cloth {cloth} not fitting any rack")
        continue

    if sum(rack) + cloth > rack_capacity:  # No space in current rack
        racks.append(rack)
        # print(f"OK Collecting rack {rack},len(racks) becoming {len(racks)}")
        rack = [cloth]
    else:  # Enough space in current rack
        rack.append(cloth)
    # print(f"rack {rack}")


if rack:  # Collect any not-yet-collected rack
    racks.append(rack)

print(len(racks))



