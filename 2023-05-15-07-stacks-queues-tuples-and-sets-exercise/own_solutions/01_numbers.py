# Not very happy with this solution
# But not happier with the in-class solution neither :P

s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
# print("OK ", s1, s2)

cmds = {
    "Add First": lambda a: s1.update(a),
    "Add Second": lambda a: s2.update(a),
    "Remove First": lambda a: s1.difference_update(a),
    "Remove Second": lambda a: s2.difference_update(a),
    "Check Subset": lambda a: print("True") if s1 < s2 or s1 > s2 else print("False")
}

for _ in range(int(input())):
    feed = input()
    feed_supported = False
    for cmd in cmds:
        if feed.startswith(cmd):
            feed_supported = True
            args = []
            if len(feed) > len(cmd):
                args = set(map(int, feed[len(cmd)::].split()))
            # print(f"OK Executing {cmd} with {args}")
            # print(f"OK before s1 {s1} s2 {s2}")
            cmds[cmd](args)
            # print(f"OK after s1 {s1} s2 {s2}")
            break
    if not feed_supported:
        # print(f"?? Unsupported feed {feed}")
        pass

print(*sorted(s1), sep=", ")
print(*sorted(s2), sep=", ")
