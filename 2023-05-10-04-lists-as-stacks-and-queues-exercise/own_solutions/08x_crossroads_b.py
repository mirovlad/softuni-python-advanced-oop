# This solution prefers arithmetics over sets

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
        time_sec = 0
        car = None
        while time_sec < green_sec and cars:
            car = cars.popleft()
            # print(f"OK time_sec {time_sec} launching car {car}")
            cars_popped += 1
            car_sec = len(car)
            time_sec += car_sec
            # print(f"OK After car time_sec {time_sec}")

        if car:
            deficit_sec = time_sec - (green_sec + free_sec)
            if deficit_sec > 0:
                crash = {
                    "car": car,
                    # "hit_idx": len(car) - hit,
                    "hit_at": car[len(car) - deficit_sec],
                }
                break


if crash:
    print("A crash happened!")
    print(f"{crash['car']} was hit at {crash['hit_at']}.")
else:
    print("Everyone is safe.")
    print(f"{cars_popped} total cars passed the crossroads.")

