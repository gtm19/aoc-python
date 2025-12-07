"""
Advent of Code solution for day 6.

See https://adventofcode.com/2025/day/6 for details.
"""

import re
from functools import reduce
from operator import add, mul, sub
from typing import Callable

funcs = {
    "*": mul,
    "+": add,
    "-": sub,
}


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        lines = f.read().splitlines()
    max_line_w = max(len(line) for line in lines)
    return [line.ljust(max_line_w) for line in lines]


def process_input(data: list[str]) -> list[list[str]]:
    expanded = list(zip(*data))
    processed = []
    to_add = [[]]

    for item in expanded:
        item = list(item)
        if not all(c == " " for c in item):
            if item[-1] in funcs:
                to_add.append(funcs[item[-1]])
                item[-1] = " "
            to_add[0].append(item)
        else:
            processed.append(tuple(to_add))
            to_add = [[]]

    processed.append(tuple(to_add))

    return processed


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    processed = process_input(data)
    total = 0
    for nums, func in processed:
        nums = list(zip(*nums))
        nums = [int(val) for d in nums if (val := "".join(d).strip())]
        to_add = reduce(func, nums)
        total += to_add
    return total


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    processed = process_input(data)
    total = 0
    for nums, func in processed:
        # nums = list(zip(*nums))
        nums = [int(val) for d in nums if (val := "".join(d).strip())]
        to_add = reduce(func, nums)
        total += to_add
    return total


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_06/input.txt")
    # input_data = read_input("tests/year2025/day_06/test_input.txt")

    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
