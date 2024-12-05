from math import floor
from util.input import read_lines


def parse_input(lines: list[str]):
    rules: dict[str, list[str]] = dict()
    instructions: list[list[str]] = []

    past_break_line = False

    for line in lines:
        if line == "":
            past_break_line = True
            continue

        if not past_break_line:
            a, b = line.split("|")
            if b in rules:
                rules[b].append(a)
            else:
                rules[b] = [a]
        else:
            pages = line.split(",")
            instructions.append(pages)

    return (rules, instructions)


def is_valid_position(
    page: str,
    instruction: list[str],
    rules: dict[str, list[str]],
    used_pages: list[str],
):
    if page not in rules:
        return True

    relevant = [x for x in rules[page] if x in instruction]

    if all(x in used_pages for x in relevant):
        return True

    return False


def is_valid_instruction(rules: dict[str, list[str]], instruction: list[str]):
    used_pages = []
    for page in instruction:
        if page in rules:
            valid = is_valid_position(page, instruction, rules, used_pages)
            if not valid:
                return False

        used_pages.append(page)

    return True


def get_middle_page(pages: list[str]):
    return pages[floor(len(pages) / 2)]


def solve_part_2(filepath):
    lines = read_lines(filepath)
    rules, instructions = parse_input(lines)
    pos_change = 0

    invalid_instructions = [
        x for x in instructions if not is_valid_instruction(rules, x)
    ]

    middle_pages = []
    for instruction in invalid_instructions:
        confirmed_pages: list[str] = []
        valid_instruction = False
        while not valid_instruction:
            for i, page in enumerate(instruction):
                # check if the position of this particular page is valid
                valid_position = is_valid_position(
                    page, instruction, rules, confirmed_pages
                )

                # if not, try moving it to end of instruction
                if not valid_position:
                    pos_change += 1
                    instruction.append(instruction.pop(i))
                    break
                # else, we know it's in the correct position
                else:
                    confirmed_pages.append(page)

            # check if the full instruction is now valid
            valid_instruction = is_valid_instruction(rules, instruction)

        middle_pages.append(get_middle_page(instruction))

    print("pos_change", pos_change)
    return sum(map(int, middle_pages))


def solve_part_1(filepath):
    lines = read_lines(filepath)

    rules, instructions = parse_input(lines)

    middle_pages = []
    for instruction in instructions:
        if is_valid_instruction(rules, instruction):
            middle_pages.append(get_middle_page(instruction))

    return sum(map(int, middle_pages))


def solve(part=1, example=False):
    filepath = f"day_05/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
