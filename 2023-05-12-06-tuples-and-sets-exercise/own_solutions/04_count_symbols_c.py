# I like this best

text = input()

for c in sorted(set(text)):
    print(f"{c}: {text.count(c)} time/s")
