# Using filter instead comprehension to practice functions
def even_odd(*args):
    command = args[-1]
    target_remainder = 0 if command == "even" else 1

    return list(filter(lambda x: x % 2 == target_remainder, args[:-1]))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))  # [2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))  # [1, 3, 5, 7, 9]
