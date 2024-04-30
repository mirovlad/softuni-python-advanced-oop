lot = set()
for _ in range(int(input())):
    direction, car_number = input().split(", ")
    if direction == "IN":
        if car_number in lot:
            pass  # print("?? Car gets IN again before going OUT")
        lot.add(car_number)
    elif direction == "OUT":
        # lot.discard(car_number) Mmmm maybe better not :P
        if car_number in lot:
            lot.remove(car_number)
        else:
            pass  # print("?? Car gets OUT before coming IN")


if lot:
    print(*lot, sep="\n")
else:
    print("Parking Lot is Empty")

