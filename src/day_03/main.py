import re
from util.input import read


def solve_part_2(filepath):
    input = read(filepath)

    pattern = r"(do\(\)|don't\(\))|mul\((\d+,\d+)\)"
    matches: list[tuple[str, str]] = re.findall(pattern, input)
    flattened = [item for sublist in matches for item in sublist]

    total = 0
    enabled = True  # is mult command enabled
    for item in flattened:
        if item == "":
            continue

        if item == "do()":
            enabled = True
        elif item == "don't()":
            enabled = False
        else:
            a, b = (int(x) for x in item.split(","))
            total += a * b if enabled else 0

    return total


def solve_part_1(filepath):
    input = read(filepath)
    pattern = r"mul\((\d+,\d+)\)"
    instructions: list[str] = re.findall(pattern, input)
    total = 0
    for instruction in instructions:
        a, b = (int(x) for x in instruction.split(","))
        total += a * b

    return total


def solve(part=1, example=False):
    if part == 1:
        filepath = f"day_03/{"example.txt" if example else "input.txt"}"
        return solve_part_1(filepath)
    else:
        filepath = f"day_03/{"example2.txt" if example else "input.txt"}"
        return solve_part_2(filepath)
