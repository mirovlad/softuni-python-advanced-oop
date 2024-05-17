# Although it pases all zero tests,
# this solution fails one of Judge's tests,
# not sure why yet
is_first = True
for s in input().split('|')[::-1]:
    if is_first:
        is_first = False
    else:
        print(" ", end="")
    print(*s.split(), sep=" ", end="")



