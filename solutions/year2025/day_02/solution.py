"""
Advent of Code solution for day 2.

See https://adventofcode.com/2025/day/2 for details.
"""

import re


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().rstrip().split(",")


def get_invalid_ids(id_range: str, repeated: bool = False) -> list[int]:
    start, stop = id_range.split("-")

    invalid_ids: list[int] = []

    for i in range(int(start), int(stop) + 1):
        i_str = str(i)

        range_end = 0 if repeated else len(i_str) // 2 - 1

        for stub_len in range((len(i_str) // 2), range_end, -1):
            regex = rf"^(\d{{{stub_len}}})\1" + ("$" if not repeated else "+$")
            if re.match(regex, str(i)):
                invalid_ids.append(i)
                break

    return invalid_ids


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    invalid_ids = [get_invalid_ids(d) for d in data]
    return sum(sum(ids) for ids in invalid_ids)


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    invalid_ids = [get_invalid_ids(d, repeated=True) for d in data]
    return sum(sum(ids) for ids in invalid_ids)


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_02/input.txt")
    # input_data = read_input("tests/year2025/day_02/test_input.txt")
    print(input_data)
    print(part_one(input_data))
    print(part_two(input_data))
