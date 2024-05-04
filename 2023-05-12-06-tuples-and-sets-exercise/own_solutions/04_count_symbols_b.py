text = input()

counts = {c: text.count(c) for c in set(text)}

for c, cnt in sorted(counts.items()):
    print(f"{c}: {cnt} time/s")
