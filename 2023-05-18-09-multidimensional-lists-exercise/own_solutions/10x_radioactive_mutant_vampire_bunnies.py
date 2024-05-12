from collections import deque

TILE_EMPTY = '.'
TILE_BUNNY = 'B'
TILE_PLAYER = 'P'

SHIFTS = {
    'U': (-1,  0),
    'D': ( 1,  0),
    'L': ( 0, -1),
    'R': ( 0,  1),
}

BUNNY_COPY_SHIFTS = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
)

def get_shifted_pos(pos, shift):
    pos1 = (pos[0] + shift[0], pos[1] + shift[1])
    return pos1


def get_tile(pos):
    if -1 < pos[0] < dim[0] and -1 < pos[1] < dim[1]:
        return lair[pos[0]][pos[1]]

    return None


def get_new_bunny_positions():
    new_bunny_positions = set()
    for r in range(dim[0]):
        for c in range(dim[1]):
            if lair[r][c] == TILE_BUNNY:
                for bunny_copy_shift in BUNNY_COPY_SHIFTS:
                    b_pos = (r, c)
                    bc_pos = get_shifted_pos(b_pos, bunny_copy_shift)
                    if -1 < bc_pos[0] < dim[0] and -1 < bc_pos[1] < dim[1]:
                        bc_tile = get_tile(bc_pos)
                        if bc_tile != TILE_BUNNY:
                            new_bunny_positions.add(bc_pos)
    return new_bunny_positions


def set_tile(pos, tile):
    lair[pos[0]][pos[1]] = tile


def print_lair():
    [print(*row, sep="") for row in lair]


dim = [int(x) for x in input().split()]

lair = []
pos = None
for r in range(dim[0]):
    row = list(input())
    lair.append(row)

    if pos is None:
        try:
            pos = (r, row.index(TILE_PLAYER))
        except ValueError:
            pass

# print(f"OK pos {pos} in lair-----------")
# print_lair()
# print("OK -----------")

shift_codes = deque(input())
# print(f"OK shift_codes {shift_codes}")

has_won = False
has_died = False
report_pos = None
while shift_codes:
    prev_pos = pos
    pos = get_shifted_pos(pos, SHIFTS[shift_codes.popleft()])
    tile = get_tile(pos)
    # print(f"OK prev_pos {prev_pos} new pos {pos} tile #{tile}# vs None #{None}#")

    set_tile(prev_pos, TILE_EMPTY)
    if tile is None:
        has_won = True
        report_pos = prev_pos
    elif tile == TILE_BUNNY:
        has_died = True
        report_pos = pos
    elif tile == TILE_EMPTY:
        set_tile(pos, TILE_PLAYER)

    new_bunny_positions = get_new_bunny_positions()
    while new_bunny_positions:
        new_bunny_pos = new_bunny_positions.pop()
        set_tile(new_bunny_pos, TILE_BUNNY)
        if new_bunny_pos == pos:
            has_died = True
            report_pos = pos

    if has_won or has_died:
        break

[print(*row, sep="") for row in lair]

if has_won:
    print(f"won: {report_pos[0]} {report_pos[1]}")
elif has_died:
    print(f"dead: {report_pos[0]} {report_pos[1]}")


