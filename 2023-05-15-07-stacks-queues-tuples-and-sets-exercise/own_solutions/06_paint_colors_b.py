from collections import deque


def recycle(piece):
    pieces.insert(len(pieces) // 2, piece)


pieces = deque(input().split())

main_colors = {"red", "yellow", "blue"}
sec_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

all_colors = main_colors.union(sec_colors.keys())
# print(f"all_colors {all_colors}")

formed_colors = []
while pieces:
    probes = []
    left_piece = pieces.popleft()
    if pieces:
        right_piece = pieces.pop()
        probes.append(left_piece + right_piece)
        probes.append(right_piece + left_piece)
    else:
        probes.append(left_piece)

    formed = False
    for probe in probes:
        if probe in all_colors:
            if probe not in formed_colors:
                formed_colors.append(probe)
                formed = True
                break
    if formed:
        continue

    left_piece = left_piece[:-1:]
    right_piece = right_piece[:-1:]

    if left_piece:
        recycle(left_piece)

    if right_piece:
        recycle(right_piece)

# print(f"formed_colors: {formed_colors}")

approved_colors = set(formed_colors)
for color in approved_colors.copy():
    if color in sec_colors:
        if not sec_colors[color] <= approved_colors:
            approved_colors.discard(color)

print([c for c in formed_colors if c in approved_colors])








