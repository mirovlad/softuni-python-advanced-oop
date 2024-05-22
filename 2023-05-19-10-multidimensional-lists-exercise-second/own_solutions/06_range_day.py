size = 5

TILE_ACTOR = "A"
TILE_TARGET = "x"
TILE_EMPTY = "."


shifts = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
}


def get_tile(pos):
    return mat[pos[0]][pos[1]]


def set_tile(pos, tile):
    mat[pos[0]][pos[1]] = tile


def is_valid_pos(pos):
    return -1 < pos[0] < size and -1 < pos[1] < size


def get_shifted_pos(pos, shift):
    return pos[0] + shift[0], pos[1] + shift[1]


# Moves the actor only if empty blocks are on the way to the pos (no jumps over obstacles)
def move_deprecated(shift, steps):
    # print(f"OK move({shift}, {steps})")
    for _ in range(steps):
        shifted_pos = get_shifted_pos(state["pos"], shift)
        if not is_valid_pos(shifted_pos):
            break

        shifted_tile = get_tile(shifted_pos)
        if shifted_tile != TILE_EMPTY:
            break

        set_tile(state["pos"], TILE_EMPTY)
        set_tile(shifted_pos, TILE_ACTOR)

        state["pos"] = shifted_pos


# Moves the actor only even over obstacles (over targets)
def move(shift, steps):
    # print(f"OK move({shift}, {steps})")
    steps_shift = steps * shift[0], steps * shift[1]
    shifted_pos = get_shifted_pos(state["pos"], steps_shift)
    if not is_valid_pos(shifted_pos):
        return

    shifted_tile = get_tile(shifted_pos)
    if shifted_tile != TILE_EMPTY:
        return

    set_tile(state["pos"], TILE_EMPTY)
    set_tile(shifted_pos, TILE_ACTOR)

    state["pos"] = shifted_pos


def move_deprecated(shift, steps):
    # print(f"OK move({shift}, {steps})")
    for _ in range(steps):
        shifted_pos = get_shifted_pos(state["pos"], shift)
        if not is_valid_pos(shifted_pos):
            break

        shifted_tile = get_tile(shifted_pos)
        if shifted_tile != TILE_EMPTY:
            break

        set_tile(state["pos"], TILE_EMPTY)
        set_tile(shifted_pos, TILE_ACTOR)

        state["pos"] = shifted_pos


def shoot(shift):
    # print(f"OK shoot({shift})")
    bullet_pos = state["pos"]
    while True:
        shifted_pos = get_shifted_pos(bullet_pos, shift)
        # print(f"OK shoot() shifted_pos {shifted_pos}")
        if not is_valid_pos(shifted_pos):
            break

        bullet_pos = shifted_pos
        bullet_tile = get_tile(bullet_pos)
        if bullet_tile == TILE_EMPTY:
            continue

        if bullet_tile == TILE_TARGET:
            set_tile(bullet_pos, TILE_EMPTY)
            targets_hit.append(bullet_pos)
            if len(targets_hit) >= targets_init_count:
                state["completed"] = True
            break


parsers = {
    "move": lambda args: move(shifts[args[1]], int(args[2])),
    "shoot": lambda args: shoot(shifts[args[1]])
}

# Having the pos in a dictionary, so that we can change it in functions without global
state = {
    "pos": None,
    "completed": None,
}

mat = []
state["pos"] = None
targets_init_count = 0
for r in range(size):
    row = input().split()
    mat.append(row)
    targets_init_count += row.count(TILE_TARGET)
    if state["pos"] is None:
        try:
            state["pos"] = (r, row.index(TILE_ACTOR))
        except ValueError:
            pass

state["completed"] = targets_init_count < 1

targets_hit = []
for _ in range(int(input())):
    if state["completed"]:
        break

    args = input().split()
    # print(f"OK args {args}")
    parsers[args[0]](args)

targets_hit_count = len(targets_hit)
if targets_hit_count < targets_init_count:
    print(f"Training not completed! {targets_init_count - targets_hit_count} targets left.")
else:
    print(f"Training completed! All {targets_hit_count} targets hit.")

# print(*targets_hit, sep="\n")  # Would have work if we were using lists, but I prefer tuples
# print(*(list(x) for x in targets_hit), sep="\n")  # Workaround by converting the tuple to lists
for pos in targets_hit:  # Another workaround
    print(f"[{pos[0]}, {pos[1]}]")

# print(f"OK pos {state["pos"]}")
# print(f"OK mat 100:")
# for row in mat:
#     print(*row, sep=" ")
