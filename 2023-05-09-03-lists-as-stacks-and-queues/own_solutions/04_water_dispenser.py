from collections import deque

dispenser_water = int(input())

clients = deque()

# Collect the clients
while True:
    inp = input()

    if inp == "Start":
        break

    clients.append(inp)

# print("OK clients", clients)

# Dispense water to clients
while True:
    inp = input()

    if inp == "End":
        break

    parts = inp.split(" ")
    len_parts = len(parts)
    # print("OK parts", parts)

    if len_parts == 1:  # Then inp must be the water quantity for the current client
        wanted_water = int(parts[0])
        if clients:
            client = clients.popleft()
            if wanted_water > dispenser_water:
                print(f"{client} must wait")
            else:  # We have enough water to dispense to the client
                dispenser_water -= wanted_water
                print(f"{client} got water")
        continue

    if len_parts == 2 and parts[0] == "refill":
        dispenser_water += int(parts[1])
        continue

print(f"{dispenser_water} liters left")
