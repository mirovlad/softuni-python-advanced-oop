def multiply(*args):
    product = 1
    for arg in args:
        if arg == 0:
            return 0
        product *= arg

    return product


# Tests
print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
