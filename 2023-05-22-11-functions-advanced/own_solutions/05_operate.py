from functools import reduce


def operate(operator, *args):

    def diff():
        return reduce(lambda a, b: a-b, args)

    ops = {
        "+": lambda: sum(args),
        "-": lambda: reduce(lambda a, b:  a - b, args),
        "*": lambda: reduce(lambda a, b: a * b, args),
        "/": lambda: reduce(lambda a, b: a / b, args),
    }

    return ops[operator]()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
