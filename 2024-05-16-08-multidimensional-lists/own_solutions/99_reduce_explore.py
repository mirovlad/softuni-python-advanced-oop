from functools import reduce


def fn_reduce(a, b):
    print(f"OK fn_reduce a #{a}# b #{b}# ")
    return a + b


# nums = [1 ,2, 3, 4, 5]
nums = [1]
# nums = []

reduced = reduce(fn_reduce, nums, 0)
print(f"OK reduced #{reduced}#")



