TILE_SANTA = "S"
TILE_KID_NAUGHTY = "X"
TILE_KID_NICE = "V"
TILE_COOKIE = "C"
TILE_EMPTY = "-"


def get_shifted_pos(pos, shift):
    return pos[0] + shift[0], pos[1] + shift[1]


def is_pos_valid(pos):
    return -1 < pos[0] < size and -1 < pos[1] < size


def get_tile(pos):
    return mat[pos[0]][pos[1]]


def set_tile(pos, tile):
    mat[pos[0]][pos[1]] = tile


def shift_santa(shift):
    pos = get_shifted_pos(state["santa_pos"], shift)
    # print(f"OK pos = {pos}")

    if not is_pos_valid(pos):
        # print(f"OK pos not valid")
        return  # Cannot go beyond edge

    tile = get_tile(pos)

    # Actually move Santa
    set_tile(state["santa_pos"], TILE_EMPTY)
    set_tile(pos, TILE_SANTA)
    state["santa_pos"] = pos

    if tile == TILE_KID_NICE:
        state["presents"] -= 1
        state["nice_kids_presented"] += 1
        return

    if state["presents"] < 1:
        return

    if tile == TILE_KID_NAUGHTY:
        return

    if tile == TILE_COOKIE:
        for probe_shift in probe_shifts:
            probe_pos = get_shifted_pos(pos, probe_shift)
            if not is_pos_valid(probe_pos):
                continue

            probe_tile = get_tile(probe_pos)

            if probe_tile == TILE_KID_NAUGHTY or probe_tile == TILE_KID_NICE:
                state["presents"] -= 1
                if probe_tile == TILE_KID_NICE:
                    state["nice_kids_presented"] += 1

                set_tile(probe_pos, TILE_EMPTY)
                if state["presents"] < 1:
                    return




shifts = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


probe_shifts = [
    shifts["left"],
    shifts["right"],
    shifts["up"],
    shifts["down"],
]

state = {
    "santa_pos": None,
    "presents": int(input()),
    "nice_kids": 0,
    "nice_kids_presented": 0,
}

size = int(input())
mat = []
for r in range(size):
    row = input().split()
    mat.append(row)
    if state["santa_pos"] is None:
        try:
            state["santa_pos"] = (r, row.index(TILE_SANTA))
        except ValueError:
            pass

    try:
        state["nice_kids"] += row.count(TILE_KID_NICE)
    except ValueError:
        pass

# print(f"OK state {state}")

if state["santa_pos"]:
    while True:
        feed = input()

        # print(f"OK iter feed {feed}")

        if feed == "Christmas morning":
            break

        if feed not in shifts:
            continue  # Not expected to happen

        # print(f"OK mat before:")
        # for row in mat:
        #     print(*row, sep=" ")
        # print(f"OK state before {state}")

        shift_santa(shifts[feed])

        # print(f"OK mat after:")
        # for row in mat:
        #     print(*row, sep=" ")
        # print(f"OK state after {state}")

        if state["presents"] < 1:
            break

# print(f"OK state {state}")

if state["presents"] < 1 and state['nice_kids'] - state['nice_kids_presented'] > 0:
    print("Santa ran out of presents!")

for row in mat:
    print(*row, sep=" ")

if state["nice_kids"] > state["nice_kids_presented"]:
    print(f"No presents for {state['nice_kids'] - state['nice_kids_presented']} nice kid/s.")
else:  # state["nice_kids"] == state["nice_kids_presented"]:
    print(f"Good job, Santa! {state['nice_kids_presented']} happy nice kid/s.")
