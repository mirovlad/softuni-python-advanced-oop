from collections import deque

clients = deque()

while True:
    line = input()
    if line == 'End':
        print(f'{len(clients)} people remaining.')
        break

    if line == 'Paid':
        while clients:
            print(clients.popleft())
        continue

    # At this point line must be a client's name
    clients.append(line)

