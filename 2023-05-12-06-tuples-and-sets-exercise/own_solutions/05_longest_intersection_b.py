# This solution prefers sets over arithmetics
# Should be OK for smaller ranges

longest = None
for _ in range(int(input())):
    r1, r2 = [tuple(map(int, r.split(','))) for r in input().split('-')]
    s1 = {n for n in range(r1[0], r1[1] + 1)}
    s2 = {n for n in range(r2[0], r2[1] + 1)}
    i = s1 & s2
    i_len = len(i)
    if longest is None or longest["len"] < i_len:
        longest = {
            "set": i,
            "len": i_len,
        }

if longest:
    print(
        f"Longest intersection is [{', '.join(str(n) for n in sorted(longest['set']))}]"
        f" with length {longest['len']}"
    )
