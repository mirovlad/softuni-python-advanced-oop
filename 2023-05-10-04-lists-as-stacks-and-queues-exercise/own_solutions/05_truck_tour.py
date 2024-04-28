from collections import deque

petrol_lpk = 1  # 1 liter petrol per km

pumps = deque()
for _ in range(int(input())):
    petrol_lt, distance_km = map(int, input().split())
    pumps.append({
        "petrol_lt": petrol_lt,
        "distance_km": distance_km,
    })

pumps_len = len(pumps)

success_idx = None
for idx in range(pumps_len):
    success = True
    probe_pumps = pumps.copy()
    tank_lt = 0
    while probe_pumps:
        pump = probe_pumps.popleft()
        tank_lt += pump["petrol_lt"]
        distance_km = pump["distance_km"]
        petrol_lt = distance_km / petrol_lpk
        if petrol_lt > tank_lt:  # Can't reach next pump
            success = False
            break

        # Travel to next pump
        tank_lt -= petrol_lt

    if success:  # Full circle completed
        success_idx = idx
        break

    # Full circle failed, "rotate" the pumps
    pumps.append(pumps.popleft())

if success_idx is None:
    print("?? Couldn't complete the circle starting off any pump")
else:
    print(idx)






