def grocery_store(**kwargs):
    def sort_key(p):
        return -p[1], -len(p[0]), p[0]

    return "\n".join(f"{p[0]}: {p[1]}" for p in sorted(kwargs.items(), key=sort_key))




print(grocery_store(
    bread=5, pasta=12, eggs=12,
))
# pasta: 12
# eggs: 12
# bread: 5

print(grocery_store(
    bread=2, pasta=2, eggs=20, carrot=1,
))
