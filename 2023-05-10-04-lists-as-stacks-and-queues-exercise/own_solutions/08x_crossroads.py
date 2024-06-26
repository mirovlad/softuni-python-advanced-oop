# This solution prefers sets over arithmetics
# As cars don't have veeeeeery long names, this is just fine

from collections import deque

green_sec = int(input())
free_sec = int(input())

cars = deque()
cars_popped = 0
crash = None
while True:
    line = input()

    if line == "END":
        break

    is_green = False
    if line == "green":
        is_green = True
    else:
        cars.append(line)

    if is_green:
        car = None
        car_chars = None
        for _ in range(green_sec):
            if not car_chars:
                if cars:
                    car = cars.popleft()
                    cars_popped += 1
                    car_chars = deque(car)

            if car_chars:
                car_chars.popleft()

        for _range in range(free_sec):
            if car_chars:
                car_chars.popleft()

        if car_chars:
            crash = {
                "car": car,
                "hit_at": car_chars.popleft()
            }
            break

if crash:
    print("A crash happened!")
    print(f"{crash['car']} was hit at {crash['hit_at']}.")
else:
    print("Everyone is safe.")
    print(f"{cars_popped} total cars passed the crossroads.")

