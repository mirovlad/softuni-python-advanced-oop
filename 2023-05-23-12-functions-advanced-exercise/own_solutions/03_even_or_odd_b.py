# Using comprehension instead filer
def even_odd(*args):
    command = args[-1]
    target_remainder = 0 if command == "even" else 1

    return [x for x in args[:-1] if x % 2 == target_remainder]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))  # [2, 4, 6]
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))  # [1, 3, 5, 7, 9]
