# Uses % operator to find key_idx, shorter code, but seems tiny bit more expensive
def math_operations(*args, **kwargs):
    ops = {
        "a": lambda value, arg: value + arg,
        "s": lambda value, arg: value - arg,
        "d": lambda value, arg: value if arg == 0 else value / arg,
        "m": lambda value, arg: value * arg,
    }

    keys = ["a", "s", "d", "m"]
    keys_len = len(keys)
    for idx, arg in enumerate(args):
        key_idx = idx % keys_len  # Instead of "crawling" key_idx up
        key = keys[key_idx]
        kwargs[key] = ops[key](kwargs[key], arg)

    kwargs = sorted(kwargs.items(), key=lambda p: (-p[1], p[0]))
    return "\n".join([f"{p[0]}: {p[1]:.1f}" for p in kwargs])




print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
# d: 33.0
# s: 15.1
# a: 9.1
# m: -58.5

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
# a: 5.1
# d: 0.0
# m: 0.0
# s: 0.0

print(math_operations(6.0, a=0, s=0, d=5, m=0))
# a: 6.0
# d: 5.0
# m: 0.0
# s: 0.0
