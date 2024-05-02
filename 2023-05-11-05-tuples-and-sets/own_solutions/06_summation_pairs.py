from collections import deque

# *Unique* integers!
nums = map(int, input().split())
target = int(input())

# Although not explicitly, the description seems to imply the number will never be negative
# Thus we can right away exclude anything higher than the target
nums = set(x for x in nums if x <= target)

pairs = []
discarded = set()
while nums:
    pair = None
    n1 = nums.pop()
    discarded.add(n1)
    # Numbers that we tried to add to n1, but didn't add up to the target
    used2 = set()
    while nums:
        n2 = nums.pop()
        if n1 + n2 == target:
            pair = (n1, n2)
            # As numbers are unique, no any other n2 can make n1+n2 = target
            break
        else:
            # Keep this one for later
            used2.add(n2)

    if pair:
        pairs.append(pair)
        discarded.add(pair[1])

    # Recover the numbers that we can still use
    nums = nums.union(used2)

for pair in pairs:
    print(f"{pair[0]} + {pair[1]} = {target}")









