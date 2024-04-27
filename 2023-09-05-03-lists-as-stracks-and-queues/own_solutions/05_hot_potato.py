from collections import deque

kids = deque(input().split(' '))
toss_num = int(input())
while len(kids) > 1:
    kids.rotate(0-(toss_num-1))
    kid = kids.popleft()
    print(f"Removed {kid}")

kid = kids.popleft()
print(f"Last is {kid}")



