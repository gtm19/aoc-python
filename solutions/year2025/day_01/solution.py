"""
Advent of Code solution for day 1.

See https://adventofcode.com/2025/day/1 for details.
"""

from collections import defaultdict
from typing import Any


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.readlines()


DIRECTIONS: dict[str, int] = {"L": -1, "R": 1}


def count_clicks(
    data: list[str],
    start_value: int = 50,
    dial_size: int = 100,
    all_clicks: bool = False,
) -> dict[int, int]:
    """
    Count the number of times each dial position is clicked.

    Parameters
    ----------
    data : list[str]
        List of movement instructions.
    start_value : int, optional
        The starting position of the dial, by default 50.
    dial_size : int, optional
        The size of the dial (number of positions), by default 100.
    all_clicks : bool, optional
        Whether to count all intermediate clicks, by default False.

    """
    dial_value: int = start_value
    counts: defaultdict[int, int] = defaultdict(lambda: 0)

    counts[dial_value] += 1

    for move in data:
        direction, amount = move[0], int(move[1:])
        increment: int = DIRECTIONS[direction]

        if all_clicks:
            for _ in range(amount):
                dial_value = (dial_value + increment) % dial_size
                counts[dial_value] += 1
        else:
            dial_value = (dial_value + increment * amount) % dial_size
            counts[dial_value] += 1

    return counts


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    counts = count_clicks(data)
    return counts[0]


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    counts = count_clicks(data, all_clicks=True)

    return counts[0]


if __name__ == "__main__":
    input_path = "solutions/year2025/day_01/input.txt"

    input_data = read_input(input_path)
    part_one_result = part_one(input_data)
    part_two_result = part_two(input_data)

    print("Part 1", part_one_result)
    print("Part 2", part_two_result)
