flat = []
for s in input().split('|')[::-1]:
    flat.extend(s.split())

print(*flat, sep=" ")
