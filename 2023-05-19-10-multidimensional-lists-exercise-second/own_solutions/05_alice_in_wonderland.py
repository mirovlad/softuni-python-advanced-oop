TILE_ALICE = "A"
TILE_RABBIT_HOLE = "R"
TILE_EMPTY = "."
TILE_PATH = "*"

BAGS_TARGET = 10

shifts = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

size = int(input())


def is_pos_valid(pos):
    return -1 < pos[0] < size and -1 < pos[1] < size


def get_shifted_pos(pos, shift):
    return pos[0] + shift[0], pos[1] + shift[1]


def set_tile(pos, tile):
    # if is_pos_valid(pos):
    mat[pos[0]][pos[1]] = tile


def get_tile(pos):
    return mat[pos[0]][pos[1]]


def debug_print_mat(title):
    print(title)
    for row in mat:
        print(*row, sep=" ")


mat = []
alice_pos = None
for r in range(size):
    row = input().split()
    mat.append(row)
    # print(f"OK row {row}")
    if alice_pos is None:
        try:
            alice_pos = (r, row.index(TILE_ALICE))
        except ValueError:
            pass

# print(f"OK alice_pos {alice_pos}")
# debug_print_mat("OK mat 00")

collected_bags = 0
if alice_pos:
    pos = alice_pos
    while True:
        feed = input()
        if feed not in shifts:
            continue

        # debug_print_mat("OK iter mat 10-------------")

        # print(f"OK pos {pos}")
        shifted_pos = get_shifted_pos(pos, shifts[feed])
        # print(f"OK shifted_pos {shifted_pos}")

        set_tile(pos, TILE_PATH)
        # debug_print_mat("OK iter mat 20")
        if not is_pos_valid(shifted_pos):
            break

        tile = get_tile(shifted_pos)
        # print(f"OK tile 10 {tile}")
        set_tile(shifted_pos, TILE_ALICE)
        # debug_print_mat("OK iter mat 30")
        pos = shifted_pos

        # print(f"OK tile 20 {tile}")

        if tile == TILE_RABBIT_HOLE:
            break

        if tile in [TILE_EMPTY, TILE_PATH, TILE_ALICE]:
            continue

        collected_bags += int(tile)

        if collected_bags >= BAGS_TARGET:
            break

# Judge wants to have a "path" tile even on the current position of Alice
set_tile(pos, TILE_PATH)

if collected_bags < BAGS_TARGET:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in mat:
    print(*row, sep=" ")
