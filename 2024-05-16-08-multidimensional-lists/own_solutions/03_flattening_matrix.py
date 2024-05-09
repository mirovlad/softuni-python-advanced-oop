flat = []
for _ in range(int(input())):
    flat.extend([int(x) for x in input().split(', ')])

print(flat)
