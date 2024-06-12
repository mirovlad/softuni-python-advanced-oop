def fill_the_box(height, length, width, *args):
    volume = height * length * width
    read = 0
    for arg in args:
        if arg == "Finish":
            break

        read += arg

    if read < volume:
        return f"There is free space in the box. You could put {volume-read} more cubes."

    return f"No more free space! You have {read - volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# There is free space in the box. You could put 13 more cubes.

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# No more free space! You have 17 more cubes.

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
# There is free space in the box. You could put 960 more cubes.
