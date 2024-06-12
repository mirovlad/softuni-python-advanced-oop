# Using comprehensions instead of map/filter
def even_odd_filter(**kwargs):

    def filter_items(how, what):
        target_remainder = 0 if how == "even" else 1
        return [x for x in what if x % 2 == target_remainder]

    # print(f"OK kwargs+ {kwargs}")
    pairs = [(p[0], filter_items(p[0], p[1])) for p in kwargs.items()]
    # print(f"OK pairs {pairs}")

    return dict(sorted(pairs, key=lambda p: -len(p[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
# {'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
# {'even': [4, 10, 2, 2], 'odd': [1, 3, 5]}
