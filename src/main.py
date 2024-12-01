import sys
import argparse
import importlib


def main():
    print("🎄Advent of Code 2024 🎄")
    parser = argparse.ArgumentParser(description="aoc2024_parser")
    parser.add_argument("-d", "--day", required=True, type=int, help="day of the month")
    parser.add_argument("-p", "--part", required=True, type=int, help="part of the day")
    parser.add_argument(
        "-e",
        "--example",
        required=False,
        type=bool,
        default=False,
        help="use example input",
    )

    args = parser.parse_args()
    module_path = f"day_{args.day:02d}.main"

    solution = None
    try:
        solution = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print("That date doesn't seem to be implemented yet :(")
        exit(1)

    answer = solution.solve(args.part, args.example)
    print(f"Day {args.day} part {args.part} {'(example)' if args.example else ''}")
    print(f"Answer: {answer}")

if __name__ == "__main__":
    sys.path.insert(0, "")
    main()
