from typing import Dict, Tuple, List

from util.input import read_lines


def calc_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])


def is_in_line(pos1, pos2, pos3):
    return (pos1[1] - pos2[1]) * (pos3[0] - pos2[0]) == (pos3[1] - pos2[1]) * (
        pos1[0] - pos2[0]
    )


def solve_part_2(filepath):
    lines = read_lines(filepath)

    grid = {}
    antennas: Dict[str, List[Tuple[int, int]]] = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid[(x, y)] = char
            if char != ".":
                if char not in antennas:
                    antennas[char] = [(x, y)]
                else:
                    antennas[char].append((x, y))

    possible_locations = set()
    for pos in grid:
        for _, positions in antennas.items():
            for pos1 in positions:
                for pos2 in positions:
                    if not is_in_line(pos1, pos2, pos):
                        continue
                    if pos1 != pos2:
                        possible_locations.add(pos)

    return len(possible_locations)


def solve_part_1(filepath):
    lines = read_lines(filepath)

    grid = {}
    antennas: Dict[str, List[Tuple[int, int]]] = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            grid[(x, y)] = char
            if char != ".":
                if char not in antennas:
                    antennas[char] = [(x, y)]
                else:
                    antennas[char].append((x, y))

    possible_locations = set()
    for pos in grid:
        for _, positions in antennas.items():
            for pos1 in positions:
                for pos2 in positions:
                    if not is_in_line(pos1, pos2, pos):
                        continue
                    if (
                        calc_distance(pos1, pos) * 2 == calc_distance(pos2, pos)
                        and pos1 != pos2
                    ):
                        possible_locations.add(pos)

    return len(possible_locations)


def solve(part=1, example=False):
    filepath = f"day_08/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
