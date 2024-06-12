def func_executor(*args):
    return "\n".join([f"{fn.__name__} - {fn(*fna)}"  for fn, fna in args])


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
# sum_numbers - 3
# multiply_numbers - 8
