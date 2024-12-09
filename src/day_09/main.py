from util.input import read
from math import floor


def solve_part_2(filepath):
    data = read(filepath).strip()

    x = []

    for i, char in enumerate(data):
        if i % 2 == 0:
            [x.append(floor(i / 2)) for _ in range(int(char))]
        else:
            [x.append(".") for _ in range(int(char))]

    def find_start_free_space(arr: list, size):
        count = 0
        for i, el in enumerate(arr):
            if el == ".":
                count += 1
                if count == size:
                    start = i - size + 1
                    return start
            else:
                count = 0

        return None

    def fill(arr: list, start, char, count):
        for i in range(start, start + count):
            arr[i] = char

        return arr

    prev = "."
    count = 0
    for a in range(len(x) - 1, -1, -1):
        print(a)
        if prev == x[a]:
            count += 1
            prev = x[a]
            continue

        if prev != x[a] and prev != ".":
            e_start = find_start_free_space(x, count + 1)
            if e_start is not None and e_start < a:
                x = fill(x, e_start, x[a + 1], count + 1)
                x = fill(x, a + 1, ".", count + 1)

        prev = x[a]
        count = 0

    checksum = 0
    for i, char in enumerate(x):
        if char != ".":
            checksum += i * int(char)

    return checksum


def solve_part_1(filepath):
    data = read(filepath).strip()

    x = []

    for i, char in enumerate(data):
        # print(i, char)
        if i % 2 == 0:
            [x.append(floor(i / 2)) for _ in range(int(char))]
        else:
            [x.append(".") for _ in range(int(char))]

    empty = [i for i in range(len(x)) if x[i] == "."]

    for a in range(len(x) - 1, -1, -1):
        if len(empty) > 0 and x[a] != ".":
            empty.sort()
            b = empty.pop(0)
            tmp = x[a]
            x[b] = tmp
            x[a] = "."
            empty.append(a)

    x = x[1:] + x[:1]

    checksum = 0
    for i, char in enumerate(x):
        if char != ".":
            checksum += i * int(char)

    return checksum


def solve(part=1, example=False):
    filepath = f"day_09/{"example.txt" if example else "input.txt"}"

    if part == 1:
        return solve_part_1(filepath)
    else:
        return solve_part_2(filepath)
