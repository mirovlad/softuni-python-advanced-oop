text = input()

counts = {c: text.count(c) for c in set(text)}

print(* [f"{c}: {cnt} time/s" for c, cnt in sorted(counts.items())], sep="\n")
