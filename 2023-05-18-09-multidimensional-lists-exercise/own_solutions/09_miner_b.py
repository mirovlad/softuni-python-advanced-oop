from collections import deque

steps = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0),
}


def get_next_pos(pos, step):
    # print(f"OK get_next_pos({pos}, {step})")
    r, c = pos[0] + step[0], pos[1] + step[1]

    if -1 < r < dim and -1 < c < dim:
        pos = (r, c)

    return pos


def get_tile(pos):
    return mat[pos[0]][pos[1]]


def set_tile(pos, tile):
    mat[pos[0]][pos[1]] = tile


TILE_REGULAR = '*'
TILE_END = 'e'
TILE_COAL = 'c'
TILE_MINER = 's'

dim = int(input())
moves = deque(input().split())

mat = []
miner_pos = None
mat_coal_count = 0
for r in range(dim):
    row = input().split()
    if miner_pos is None:
        try:
            miner_pos = (r, row.index(TILE_MINER))
        except ValueError:
            pass
    mat_coal_count += row.count(TILE_COAL)
    mat.append(row)

# print(f"OK mat:")
# [print(*row, sep=" ") for row in mat]

# print(f"OK miner_pos {miner_pos} mat_coal_count {mat_coal_count}")


has_stepped_on_end = False
is_coal_collected = mat_coal_count < 1
while moves:
    old_miner_pos = miner_pos
    miner_pos = get_next_pos(miner_pos, steps[moves.popleft()])

    # Commented out in favour of check for TILE_MINER further down
    # if next_miner_pos == miner_pos: # We are on the same place as before
    #     continue

    tile = get_tile(miner_pos)
    # print(f"OK miner_pos {miner_pos} tile {tile}")

    if tile == TILE_END:
        set_tile(old_miner_pos, TILE_REGULAR)
        set_tile(miner_pos, TILE_MINER)
        has_stepped_on_end = True
        break

    if tile == TILE_MINER: # We are on the same place as before
        continue

    if tile == TILE_REGULAR:
        set_tile(old_miner_pos, TILE_REGULAR)
        set_tile(miner_pos, TILE_MINER)
        continue

    if tile == TILE_COAL:
        set_tile(old_miner_pos, TILE_REGULAR)
        set_tile(miner_pos, TILE_MINER)
        mat_coal_count -= 1
        if mat_coal_count < 1:
            is_coal_collected = True
            break


if has_stepped_on_end:
    print(f"Game over! ({miner_pos[0]}, {miner_pos[1]})")
elif is_coal_collected:
    print(f"You collected all coal! ({miner_pos[0]}, {miner_pos[1]})")
else:
    print(f"{mat_coal_count} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")