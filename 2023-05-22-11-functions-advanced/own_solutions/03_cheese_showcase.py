def sorting_cheeses(**kwargs):
    kvp_sorted = sorted(kwargs.items(), key=lambda kvp: (0-len(kvp[1]), kvp[0]))
    print(f"OK kvp_sorted {kvp_sorted}")

    result = ""
    for cheese, pieces in kvp_sorted:
        if result:
            result += "\n"
        result += cheese + "\n"
        result += "\n".join(map(str, sorted(pieces, reverse=True)))

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)