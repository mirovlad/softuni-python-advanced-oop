even = set()
odd = set()
for idx in range(int(input())):
    s = sum([ord(c) for c in input()]) // (idx + 1)
    even.add(s) if s % 2 == 0 else odd.add(s)

s_even = sum(even)
s_odd = sum(odd)

if s_odd > s_even:
    print(*(odd - even), sep=", ")
elif s_odd < s_even:
    print(*(odd ^ even), sep=", ")
else:  # s_odd == s_even:
    print(*(odd | even), sep=", ")
