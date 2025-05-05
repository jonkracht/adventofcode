import sys, itertools

infile = sys.argv[1] if len(sys.argv) >= 2 else "./data/21.in"

codes = open(infile).read().strip().split()
# print(codes)


# Button locations, expressed in row/column notation
numpad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}

dirpad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}

start_loc = (3, 2)  # 'A'


def get_numpad_actions(chars: str, current: tuple) -> list:
    """Determine numpad actions."""

    cmd = []

    for cc in list(chars):

        target = numpad[cc]
        # print(f"\nCurrent location is {current}.  Target button is {cc} which is located at {target}.")

        di, dj = target[0] - current[0], target[1] - current[1]
        # print(f"Delta is ({di}, {dj})")

        if di >= 0:
            isym = "v"
        else:
            isym = "^"
        if dj >= 0:
            jsym = ">"
        else:
            jsym = "<"

        # Avoid routing over blank button
        if di > 0:  # moving downward on keypad
            for _ in range(abs(dj)):
                cmd.append(jsym)
            for _ in range(abs(di)):
                cmd.append(isym)
        else:
            for _ in range(abs(di)):
                cmd.append(isym)
            for _ in range(abs(dj)):
                cmd.append(jsym)

        # print(f"Command following this button:  {cmd}")

        cmd.append("A")
        current = target  # update location

    # print(f"\n\n*** Complete numpad command is ***\n{cmd}")
    return cmd


def get_dirpad_actions(chars: list, current: tuple):
    """Determine directional keypad actions."""

    # print(f"\n\n*** Calling 'get_dirpad_actions' with ***\n{chars}")

    cmd = []

    for cc in list(chars):

        target = dirpad[cc]
        # print(f"\nCurrent location is {current}.  Target button is {cc} which is located at {target}.")

        di, dj = target[0] - current[0], target[1] - current[1]
        # print(f"Delta is ({di}, {dj})")

        if di >= 0:
            isym = "v"
        else:
            isym = "^"
        if dj >= 0:
            jsym = ">"
        else:
            jsym = "<"

        if di > 0:
            for _ in range(abs(di)):
                cmd.append(isym)
            for _ in range(abs(dj)):
                cmd.append(jsym)

        else:
            for _ in range(abs(dj)):
                cmd.append(jsym)
            for _ in range(abs(di)):
                cmd.append(isym)

        # print(f"Command following this button:  {cmd}")
        cmd.append("A")

        current = target

    return cmd


# codes = ['029A', '980A', '179A', '456A', '379A']
codes = ["379A"]
presses = {}

for c in codes:
    print(f"\n\n*** Code {c} ***")

    numpad_moves = get_numpad_actions(c, (3, 2))
    dirpad_moves_1 = get_dirpad_actions(numpad_moves, (0, 2))
    dirpad_moves_2 = get_dirpad_actions(dirpad_moves_1, (0, 2))

    print(f"\nNumpad moves:\n{''.join(numpad_moves)}")
    print(f"({len(numpad_moves)})")

    print(f"\nDirpad moves 1:\n{''.join(dirpad_moves_1)}")
    print(f"({len(dirpad_moves_1)})")

    print(f"\nDirpad moves 2:\n{''.join(dirpad_moves_2)}")
    print(f"({len(dirpad_moves_2)})")

    presses[c] = dirpad_moves_2


print("\n*** Aggregating individual codes ***")
p1_complexity = 0

for k, v in presses.items():
    numeric = int(k.split("A")[0])
    ct = len(v)
    print(f"{k}:  {ct}  ({numeric} * {ct} = {numeric*ct})")
    p1_complexity += numeric * ct

print(f"\n{'Solution to Part 1:':<20} {p1_complexity}")
