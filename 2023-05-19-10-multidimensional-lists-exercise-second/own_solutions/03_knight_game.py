import math

TILE_KNIGHT = "K"
TILE_EMPTY = "0"


def print_mat(title):
    print(title)
    [print(*row, sep="") for row in mat]


def get_targeted_knights_count(pos):
    r, c = pos
    count = 0
    for dr, dc in ((-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)):
        if 0 <= r + dr < size and 0 <= c + dc < size:
            if mat[r + dr][c + dc] == TILE_KNIGHT:
                count += 1
    return count


def get_max_targeting_knight():
    max_targeting_knight = {
        "pos": None,
        "targets_count": -math.inf
    }

    for r in range(size):
        for c in range(size):
            if mat[r][c] == TILE_KNIGHT:
                count = get_targeted_knights_count((r, c))
                if count > max_targeting_knight["targets_count"]:
                    max_targeting_knight["targets_count"] = count
                    max_targeting_knight["pos"] = (r, c)
    return max_targeting_knight


def set_mat_tile(pos, tile):
    mat[pos[0]][pos[1]] = tile


size = int(input())
mat = [list(input()) for _ in range(size)]

removed_knights_count = 0
while True:
    max_targeting_knight = get_max_targeting_knight()
    if max_targeting_knight["targets_count"] <= 0:
        # There was no any knight on the board (to start with),
        # or no knight is targeting other knights
        break

    # Remove the knight
    set_mat_tile(max_targeting_knight["pos"], TILE_EMPTY)
    removed_knights_count += 1

print(removed_knights_count)



