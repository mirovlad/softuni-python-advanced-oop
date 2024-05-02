from collections import deque

# *Unique* integers!
nums = map(int, input().split())
target = int(input())

# Although not explicitly, the description seems to imply the number will never be negative
# Thus we can right away exclude anything higher than the target
nums = set(x for x in nums if x <= target)

pairs = []
while nums:
    pair = None
    n1 = nums.pop()
    # To hold the n2 numbers that we try to pair with n1, but didn't give the target
    used2 = set()
    while nums:
        n2 = nums.pop()
        if n1 + n2 == target:
            pairs.append((n1, n2))
            # As numbers are unique, no any other n2 can make n1+n2 = target, we can break
            break
        else:
            # n2 didn't pair with n1, so keep n2 for further use
            used2.add(n2)

    # Recover the n2-s that we can still use
    nums = nums.union(used2)

for pair in pairs:
    print(f"{pair[0]} + {pair[1]} = {target}")









