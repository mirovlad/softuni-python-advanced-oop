# Own solution from 2023

# Tuple to "prevent" changing the input after taking it :P
numbers = (float(node) for node in input().split())

counts = {}
for number in numbers:
    number_key = f"{number:.1f}"
    if number_key not in counts:
        counts[number_key] = 0
    counts[number_key] += 1

for number_key, count in counts.items():
    print(f"{number_key} - {count} times")