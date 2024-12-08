from util.input import read_lines
from typing import Tuple


def in_bounds(pos: Tuple[int, int], grid: dict[Tuple[int, int], str]):
    return pos in grid


def get_next_pos(pos: Tuple[int, int], direction: int):
    step = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]
    return (pos[0] + step[0], pos[1] + step[1])


def check_if_loop(
    grid: dict[Tuple[int, int], str], pos: Tuple[int, int], direction: int
):
    visited: set[Tuple[Tuple[int, int], int]] = set()

    while True:
        # If our path took us out of bounds, we're not in a loop
        if not in_bounds(pos, grid):
            return False

        if (pos, direction) in visited:
            return True
        else:
            visited.add((pos, direction))

        next_pos = get_next_pos(pos, direction)
        if grid.get(next_pos) == "#":
            direction = (direction + 1) % 4
            continue

        pos = next_pos


def solve_part_2(filepath):
    lines = read_lines(filepath)

    grid: dict[Tuple[int, int], str] = {}
    starting_pos: Tuple[int, int] = (0, 0)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[(i, j)] = char
            if char == "^":
                starting_pos = (i, j)

    pos = starting_pos
    possible_locations = set()
    direction = 0  # up 0, right 1, down 2, left 3
    while True:
        tmp_grid = grid.copy()
        tmp_grid[pos] = "#"

        if check_if_loop(tmp_grid, starting_pos, 0):
            possible_locations.add(pos)

        next_pos = get_next_pos(pos, direction)
        if not in_bounds(next_pos, grid):
            break

        if grid.get(next_pos) == "#":
            direction = (direction + 1) % 4
            continue

        pos = next_pos

    return len(possible_locations)


def solve_part_1(filepath):
    lines = read_lines(filepath)

    grid = {}
    pos: Tuple[int, int] = 0, 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            grid[(i, j)] = char
            if char == "^":
                pos = (i, j)

    direction = 0  # up 0, right 1, down 2, left 3

    while True:
        next_pos = get_next_pos(pos, direction)
        if grid.get(next_pos) == "#":
            direction = (direction + 1) % 4
            continue
        else:
            grid[pos] = "X"

        pos = next_pos

        if not in_bounds(pos, grid):
            break

    return sum(1 for value in grid.values() if value == "X")


def solve(part=1, example=False):
    filepath = f"day_06/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
