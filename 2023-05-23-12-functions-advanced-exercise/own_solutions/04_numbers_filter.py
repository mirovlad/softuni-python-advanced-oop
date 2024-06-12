# Using map/filter instead of comprehensions to practice functions

def even_odd_filter(**kwargs):

    def filter_items(how, what):
        target_remainder = 0 if how == "even" else 1
        return list(filter(lambda x: x % 2 == target_remainder, what))

    # print(f"OK kwargs {kwargs}")
    pairs = list(map(lambda p: (p[0], filter_items(p[0], p[1])), kwargs.items()))
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
