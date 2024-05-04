# This solution prefers arithmetics over sets
# Would be better in case ranges are very large

longest = None
for _ in range(int(input())):
    r1, r2 = [tuple(map(int, r.split(','))) for r in input().split('-')]
    # print(r1, r2)
    i_start = max(r1[0], r2[0])
    i_end = min(r1[1], r2[1])
    if i_start > i_end:
        continue  # No intersection, skip, requirements say this never happens

    i_len = i_end - i_start + 1
    if longest is None or longest["len"] < i_len:
        longest = {
            "ranges": (r1, r2),
            "start": i_start,
            "end": i_end,
            "len": i_len,
        }

if longest:
    print(
        f"Longest intersection is [{', '.join(str(n) for n in range(longest['start'], longest['end'] + 1))}]"
        f" with length {longest['len']}"
    )
