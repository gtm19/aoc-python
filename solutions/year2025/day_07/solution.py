"""
Advent of Code solution for day 7.

See https://adventofcode.com/2025/day/7 for details.
"""

from collections import defaultdict


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


def process_beams(data: list[str]) -> tuple[int, int]:
    beams: defaultdict[int, int] = defaultdict(int)
    splits: int = 0

    for row in data:
        for i, c in enumerate(row):
            if c == "S":
                beams[i] = 1
            if c == "^":
                if i not in beams:
                    continue
                beams[i - 1] += beams[i]
                beams[i + 1] += beams[i]
                del beams[i]
                splits += 1

    return splits, sum(beams.values())


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    splits, _ = process_beams(data)
    return splits


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    _, n_beams = process_beams(data)
    return n_beams


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_07/input.txt")

    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
