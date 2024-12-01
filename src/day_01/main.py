from util.input import read_lines

def solve_part_2(filepath):
    lines = read_lines(filepath)

    left_list: list[int] = []
    right_map: dict[int, int] = {}

    for line in lines:
        left_str, right_str = line.split("   ")
        left_list.append(int(left_str))
        right = int(right_str)

        right_map.setdefault(right, 0)
        right_map[right] = right_map[right] + 1

    similarity_score = 0
    for i in range(len(left_list)):
        left = left_list[i]
        count = right_map.get(left)
        if count is not None:
            similarity_score += count * left

    return similarity_score

def solve_part_1(filepath):
    lines = read_lines(filepath)

    left_list = []
    right_list = []

    for line in lines:
        left_str, right_str = line.split("   ")
        left_list.append(int(left_str))
        right_list.append(int(right_str))

    left_list.sort()
    right_list.sort()

    distance = 0
    for left, right in zip(left_list, right_list):
        distance += abs(left - right)

    return distance

def solve(part=1, example=False):
    filename = "day_01/example.txt" if example else "day_01/input.txt"
    filepath = f"{filename}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
