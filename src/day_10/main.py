from collections import deque
from util.input import read_lines


def solve_part_2(filepath):
    lines = read_lines(filepath)

    starting_points = []
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            elevation = int(char)
            grid[(x, y)] = elevation
            if elevation == 0:
                starting_points.append((x, y))

    score = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for start in starting_points:
        stack = deque()
        stack.append((start, [start]))
        all_paths = []
        target = 9

        while len(stack) > 0:
            pos, path = stack.pop()

            if pos in grid and grid[pos] == target:
                all_paths.append(path)
                continue

            for new_pos in [(pos[0] + d[0], pos[1] + d[1]) for d in directions]:
                if new_pos not in grid:
                    continue

                if grid[new_pos] - grid[pos] != 1:
                    continue

                stack.append((new_pos, path + [new_pos]))

        score += len(all_paths)

    return score


def solve_part_1(filepath):
    lines = read_lines(filepath)

    starting_points = []
    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            elevation = int(char)
            grid[(x, y)] = elevation
            if elevation == 0:
                starting_points.append((x, y))

    score = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for start in starting_points:
        stack = deque()
        stack.append(start)
        visited = set()  # all visited points
        found = set()  # found 9s
        target = 9

        while len(stack) > 0:
            pos = stack.pop()
            visited.add(pos)

            if pos in grid and grid[pos] == target:
                found.add(pos)
                continue

            for new_pos in [(pos[0] + d[0], pos[1] + d[1]) for d in directions]:
                if new_pos in visited or new_pos not in grid:
                    continue

                if grid[new_pos] - grid[pos] != 1:
                    continue

                stack.append(new_pos)

        score += len(found)

    return score


def solve(part=1, example=False):
    filepath = f"day_10/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
