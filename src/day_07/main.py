from util.input import read_lines
from itertools import product


def add_or_mult_by_operator(op: str, num1: int, num2: int):
    if op == "+":
        return num1 + num2
    elif op == "|":
        return int(str(num1) + str(num2))
    else:
        return num1 * num2


def check_nums(test_value: int, nums: list[int], part_2=False):
    operators = "+*" if not part_2 else "+*|"
    permutations = product(operators, repeat=(len(nums) - 1))
    for perm in permutations:
        result = nums[0]
        for i, num in enumerate(nums[1:]):
            result = add_or_mult_by_operator(perm[i], result, num)
        if result == test_value:
            return True

    return False


def solve_part_2(filepath):
    lines = read_lines(filepath)

    sum = 0

    for line in lines:
        test_value_str, num_str = line.split(":")
        test_value = int(test_value_str)
        nums = [int(x) for x in num_str.split()]

        if check_nums(test_value, nums, True):
            sum += test_value

    return sum


def solve_part_1(filepath):
    lines = read_lines(filepath)

    sum = 0

    for line in lines:
        test_value_str, num_str = line.split(":")
        test_value = int(test_value_str)
        nums = [int(x) for x in num_str.split()]

        if check_nums(test_value, nums):
            sum += test_value

    return sum


def solve(part=1, example=False):
    filepath = f"day_07/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
