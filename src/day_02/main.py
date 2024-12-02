from util.input import read_lines


def is_sorted(levels):
    # check if list is already sorted, or if reversed list is sorted
    if sorted(levels) == levels or sorted(levels, reverse=True) == levels:
        return True

    return False


def is_gradual(levels):
    # check if max distance between adjacent levels is max 3 min 1
    return all(3 >= abs(a - b) > 0 for a, b in zip(levels, levels[1:]))


def is_valid(levels):
    return is_sorted(levels) and is_gradual(levels)


def solve_part_2(filepath):
    lines = read_lines(filepath)
    total_valid = 0

    for line in lines:
        levels = list(map(int, line.split()))

        # base case, check if line of levels is valid without removals
        if is_valid(levels):
            total_valid += 1
        # else, check for all permutations where 1 item is removed
        else:
            for i in range(len(levels)):
                if is_valid(levels[:i] + levels[i + 1 :]):
                    total_valid += 1
                    break

    return total_valid


def solve_part_1(filepath):
    lines = read_lines(filepath)
    total_valid = 0
    for line in lines:
        levels = list(map(int, line.split()))
        total_valid += 1 if is_valid(levels) else 0
    return total_valid


def solve(part=1, example=False):
    filepath = f"day_02/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
