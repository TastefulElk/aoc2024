from util.input import read_lines
from collections import deque
from typing import List, Tuple


def bfs(grid, y, x):
    search = grid[y][x]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(y, x)])
    found = []
    while len(queue) > 0:
        y, x = queue.popleft()
        if grid[y][x] != search:
            continue
        found.append((y, x))
        grid[y][x] = None
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                queue.append((ny, nx))

    return found


def count_sides(region: List[Tuple[int, int]], grid: List[List[str]]):
    # 1 corner = 1 side so find all corners
    corners = 0
    for y, x in region:
        # external corners
        if (y - 1, x) not in region and (y, x - 1) not in region:
            corners += 1

        if (y - 1, x) not in region and (y, x + 1) not in region:
            corners += 1

        if (y + 1, x) not in region and (y, x - 1) not in region:
            corners += 1

        if (y + 1, x) not in region and (y, x + 1) not in region:
            corners += 1

        # internal corners
        if (
            (y - 1, x) in region
            and (y, x - 1) in region
            and (y - 1, x - 1) not in region
        ):
            corners += 1

        if (
            (y - 1, x) in region
            and (y, x + 1) in region
            and (y - 1, x + 1) not in region
        ):
            corners += 1

        if (
            (y + 1, x) in region
            and (y, x - 1) in region
            and (y + 1, x - 1) not in region
        ):
            corners += 1

        if (
            (y + 1, x) in region
            and (y, x + 1) in region
            and (y + 1, x + 1) not in region
        ):
            corners += 1

    return corners


def solve_part_2(filepath):
    lines = read_lines(filepath)

    grid = []

    for line in lines:
        grid.append(list(line))

    # print(grid)
    seen = set()
    regions = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in seen:
                continue

            found = bfs(grid, y, x)
            # print(grid)
            [seen.add(f) for f in found]
            regions.append(found)

    cost = 0
    # print(grid)
    for region in regions:
        area = len(region)
        sides = count_sides(region, grid)

        cost += area * sides
    return cost


def solve_part_1(filepath):
    lines = read_lines(filepath)

    grid = []

    for line in lines:
        grid.append(list(line))

    seen = set()
    regions = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in seen:
                continue
            found = bfs(grid.copy(), y, x)
            [seen.add(f) for f in found]
            regions.append(found)

    cost = 0
    for region in regions:
        area = len(region)
        # perimeter is the number of cells that are adjacent to a cell that is not in the region
        perimeter = 0
        for y, x in region:
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny, nx = y + dy, x + dx
                if (ny, nx) not in region:
                    perimeter += 1

        cost += area * perimeter
    return cost


def solve(part=1, example=False):
    filepath = f"day_12/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
