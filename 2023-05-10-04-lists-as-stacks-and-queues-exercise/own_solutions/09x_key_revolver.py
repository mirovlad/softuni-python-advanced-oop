from collections import deque

ppb = int(input())  # price per bullet
barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intel = int(input())

used_bullets_cnt = 0
used_barrel_bullets_cnt = 0
while locks and bullets:

    lock = locks.popleft()
    bullet = bullets.pop()
    used_bullets_cnt += 1
    used_barrel_bullets_cnt += 1

    if lock >= bullet:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    # Reloading only possible if bullets still left
    if bullets and used_barrel_bullets_cnt == barrel_size:
        print("Reloading!")
        used_barrel_bullets_cnt = 0

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    bullets_cost = used_bullets_cnt * ppb
    earned = intel - bullets_cost
    print(f"{len(bullets)} bullets left. Earned ${earned}")



