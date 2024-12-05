from util.input import read_lines


def solve_part_2(filepath):
    lines = read_lines(filepath)
    found = 0

    for r, row in enumerate(lines):
        for c, _ in enumerate(row):

            def in_bounds(r, c):
                return r > 0 and c > 0 and r + 1 < len(lines) and c + 1 < len(row)

            def valid_chars(c1, c2):
                return c1 == "M" and c2 == "S" or c1 == "S" and c2 == "M"

            def is_x_mas(r, c):
                if lines[r][c] != "A" or not in_bounds(r, c):
                    return False

                ul = lines[r - 1][c - 1]
                ur = lines[r - 1][c + 1]
                ll = lines[r + 1][c - 1]
                lr = lines[r + 1][c + 1]

                if valid_chars(ul, lr) and valid_chars(ur, ll):
                    return True

                return False

            if is_x_mas(r, c):
                found += 1

    return found


def solve_part_1(filepath):
    lines = read_lines(filepath)
    found = 0
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col == "X":
                print(f"r {r} c {c}, lines {len(lines)} rows {len(row)}")
                # vertical
                if r >= 3 and lines[r - 1][c] == "M":
                    if lines[r - 2][c] == "A":
                        if lines[r - 3][c] == "S":
                            found += 1

                if r + 3 <= (len(lines) - 1) and lines[r + 1][c] == "M":
                    if lines[r + 2][c] == "A":
                        if lines[r + 3][c] == "S":
                            found += 1

                # horizontal
                if c >= 3:
                    if lines[r][c - 1] == "M":
                        if lines[r][c - 2] == "A":
                            if lines[r][c - 3] == "S":
                                found += 1

                if c + 3 <= len(row) - 1 and lines[r][c + 1] == "M":
                    if lines[r][c + 2] == "A":
                        if lines[r][c + 3] == "S":
                            found += 1

                # diagonal
                if r >= 3 and c >= 3:
                    if lines[r - 1][c - 1] == "M":
                        if lines[r - 2][c - 2] == "A":
                            if lines[r - 3][c - 3] == "S":
                                found += 1

                if r + 3 <= (len(lines) - 1) and c + 3 <= len(row) - 1:
                    if lines[r + 1][c + 1] == "M":
                        if lines[r + 2][c + 2] == "A":
                            if lines[r + 3][c + 3] == "S":
                                found += 1

                if r >= 3 and c + 3 <= len(row) - 1:
                    if lines[r - 1][c + 1] == "M":
                        if lines[r - 2][c + 2] == "A":
                            if lines[r - 3][c + 3] == "S":
                                found += 1

                if r + 3 <= (len(lines) - 1) and c >= 3:
                    if lines[r + 1][c - 1] == "M":
                        if lines[r + 2][c - 2] == "A":
                            if lines[r + 3][c - 3] == "S":
                                found += 1
    return found


def solve(part=1, example=False):
    filepath = f"day_04/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
