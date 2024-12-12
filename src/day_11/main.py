from util.input import read
from collections import deque
from collections import Counter


def solve_part_2(filepath):
    stones = Counter(map(int, read(filepath).split()))

    for _ in range(75):
        new_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
                continue

            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                mid = len(stone_str) // 2
                lh, rh = int(stone_str[:mid]), int(stone_str[mid:])
                new_stones[lh] += count
                new_stones[rh] += count
                continue

            new_stones[stone * 2024] += count
        stones = new_stones

    return sum(stones.values())


def solve_part_1(filepath):
    stones = [int(x) for x in read(filepath).split()]

    for i in range(75):
        print(i)
        queue = deque(stones)
        stones = []
        while len(queue) > 0:
            stone = queue.popleft()
            if stone == 0:
                stones.append(1)
                continue

            stone_str = str(stone)
            if len(stone_str) % 2 == 0:
                mid = len(stone_str) // 2
                lh, rh = stone_str[:mid], stone_str[mid:]
                stones.append(int(lh))
                stones.append(int(rh))
                continue

            stones.append(stone * 2024)

    return len(stones)


def solve(part=1, example=False):
    filepath = f"day_11/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
