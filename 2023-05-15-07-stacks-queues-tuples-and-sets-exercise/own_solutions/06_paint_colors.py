from collections import deque

nodes = deque(input().split())

main = {"red", "yellow", "blue"}
secondary = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

formed = []
while nodes:
    # print("OK nodes", nodes)
    first = nodes.popleft()
    last = nodes.pop() if nodes else ""

    probe = first + last
    # print(f"OK first #{first}# last #{last}# probe #{probe}#")
    if probe in main or probe in secondary:
        # print(f"OK probe collected")
        formed.append(probe)
        continue

    probe = last + first
    # print(f"OK last #{last}# first #{first}# probe #{probe}#")
    if probe in main or probe in secondary:
        # print(f"OK probe collected")
        formed.append(probe)
        continue

    if len(first) > 1:
        nodes.insert(len(nodes) // 2, first[:-1:])
        # print("OK reinserted first")

    if len(last) > 1:
        nodes.insert(len(nodes) // 2, last[:-1:])
        # print("OK reinserted last")

# print(f"OK formed {formed}")

formed_set = set(formed)
for s, m in secondary.items():
    if s in formed and not m <= formed_set:
        formed.remove(s)

print(formed)
