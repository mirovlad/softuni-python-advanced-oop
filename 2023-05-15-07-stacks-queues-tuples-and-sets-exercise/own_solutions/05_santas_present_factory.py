from collections import deque

materials = deque([int(x) for x in input().split()])
magics = deque([int(x) for x in input().split()])

present_magics = [
    {"present": "Doll", "magic": 150},
    {"present": "Wooden train", "magic": 250},
    {"present": "Teddy bear", "magic": 300},
    {"present": "Bicycle", "magic": 400},
]

pm_map = {pm["magic"]: pm["present"] for pm in present_magics}

toys = {}
while materials and magics:
    material = materials.pop()
    magic = magics.popleft()

    eff_magic = material * magic

    if eff_magic == 0:
        if material != 0:
            materials.append(material)
        if magic != 0:
            magics.appendleft(magic)

    if eff_magic in pm_map:
        name = pm_map[eff_magic]
        if name not in toys:
            toys[name] = 0
        toys[name] += 1
        continue

    if eff_magic < 0:
        materials.append(material + magic)
        continue

    if eff_magic > 0:
        materials.append(material + 15)
        continue

is_done = False
if "Doll" in toys and "Wooden train" in toys:
    is_done = True
elif "Teddy bear" in toys and "Bicycle" in toys:
    is_done = True

if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left: ", end="")
    materials.reverse()
    print(*materials, sep=", ")

if magics:
    print("Magic left: ", end="")
    print(*magics, sep=", ")


for name, amount in dict(sorted(toys.items())).items():
    print(f"{name}: {amount}")


