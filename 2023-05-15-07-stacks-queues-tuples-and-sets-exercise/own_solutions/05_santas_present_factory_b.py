# Using sets to check if toys needed are done

from collections import deque

materials = deque([int(n) for n in input().split()])
magics = deque([int(n) for n in input().split()])

potential_to_toy = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

toy_counts = {}
while materials and magics:
    material = materials.pop()
    magic = magics.popleft()

    if material == 0 or magic == 0:
        # Put any of the non-zeroes back
        if material:
            materials.append(material)  # Put it back
        if magic:
            magics.appendleft(magic)  # Put it back
        continue

    potential = material * magic  # Always non-zero

    if potential in potential_to_toy:
        toy = potential_to_toy[potential]
        toy_counts[toy] = 1 + (toy_counts[toy] if toy in toy_counts else 0)
        continue

    if potential < 0:
        # Not clear on which side of the materials we have to add the sum
        material += magic
        materials.append(material)
        #materials.appendleft(material)
        continue

    if potential > 0:  # At this point must be the case anyway
        # Magic value remains wasted, only re-use adjusted material
        material += 15
        materials.append(material)
        #materials.appendleft(material)


toys = set(toy_counts.keys())

if {"Doll", "Wooden train"} <= toys or {"Teddy bear", "Bicycle"} <= toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials.reverse()
    print("Materials left: " + ", ".join(str(m) for m in materials))

if magics:
    print("Magic left: " + ", ".join(str(m) for m in magics))

for toy in sorted(toys):
    print(f"{toy}: {toy_counts[toy]}")
