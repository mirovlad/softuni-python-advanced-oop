# Own solution from 2023

import collections

pumps_count = int(input())
pumps = collections.deque()
for idx in range(pumps_count):
    nodes = input().split()
    pump = {
        "fuel": int(nodes[0]),
        "distance": int(nodes[1])
    }
    pumps.append(pump)

pumps_rotated = pumps.copy()
for probe_idx in range(pumps_count):
    pumps_probe = pumps_rotated.copy()
    tank_fuel = 0
    completed = True
    while pumps_probe:
        pump = pumps_probe.popleft()
        tank_fuel += pump["fuel"]  # Load the fuel from the pump
        distance = pump["distance"]
        if distance > tank_fuel:  # Not enough fuel in the tank to cover the distance
            completed = False
            break
        tank_fuel -= distance  # Spend the fuel to cover the distance

    if completed:  # Managed to complete the circle, no more probes needed
        break
    pumps_rotated.rotate(-1)

if completed:
    print(probe_idx)





