# This solution prefers sets over arithmetics, similar to B solution
# I.e. should still be OK for smaller ranges
# Pro vs B: A bit shorter code
# Con vs B: len of the longest set is recalculated multiple times

longest = None
for _ in range(int(input())):
    r1, r2 = [tuple(map(int, r.split(','))) for r in input().split('-')]
    s1 = {n for n in range(r1[0], r1[1] + 1)}
    s2 = {n for n in range(r2[0], r2[1] + 1)}
    i = s1 & s2
    if longest is None or len(longest) < len(i):
        longest = i


if longest:
    print(
        f"Longest intersection is [{', '.join(str(n) for n in sorted(longest))}]"
        f" with length {len(longest)}"
    )
