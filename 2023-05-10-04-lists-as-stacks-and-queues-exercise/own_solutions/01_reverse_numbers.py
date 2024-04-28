from collections import deque

# entries = deque([int(x) for x in input().split()])
entries = deque(input().split())  # Converting to integers not really needed
while entries:
    print(entries.pop(), end=" ")
