from functools import reduce


def fn_reduce(p, n):
    # print(f"OK fn_reduce p #{p}# n #{n}#")
    p[n[0]] += int(n[1])
    return p


size = tuple([int(x) for x in input().split(', ')])

sums = [0 for x in range(size[1])]
for _ in range(size[0]):
    sums = reduce(fn_reduce, enumerate(input().split()), sums)

print(*sums, sep="\n")
