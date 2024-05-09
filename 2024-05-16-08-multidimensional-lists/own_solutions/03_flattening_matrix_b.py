rows_count = int(input())

flattened = []
[flattened.extend([int(n) for n in input().split(", ")]) for _ in range(rows_count)]

print(flattened)

