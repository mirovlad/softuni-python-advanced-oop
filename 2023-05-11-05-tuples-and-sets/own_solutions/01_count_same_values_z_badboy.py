# !! Doesn't satisfy Judge, but I like it :P
# Empirically found Judge expects the numbers and their counts in the output
# to be in the order of their appearance in the input.
# This requirement is not explicitly mentioned in the problem's description

# Tuple to "prevent" changing the input after taking it :P
numbers = tuple(map(float, input().split()))
rounded = tuple(f"{x:.1f}" for x in numbers)

unique = set(rounded)

counts = {un: rounded.count(un) for un in unique}

for un, cnt in counts.items():
    print(f"{un} - {cnt} times")



