"""
Advent of Code solution for day 9.

See https://adventofcode.com/2025/day/9 for details.
"""

from itertools import pairwise
from typing import TypeAlias


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


point: TypeAlias = tuple[int, int]


def get_largest_area(data: list[str], exclude_overlaps: bool = False) -> int:
    """Calculate the largest area from the given points."""
    tiles: list[point] = list[point](
        tuple([int(x), int(y)]) for line in data for x, y in (line.split(","),)
    )
    areas = []
    for i in range(len(tiles)):
        for j in range(i):
            x_1, y_1 = tiles[i]
            x_2, y_2 = tiles[j]
            if x_1 > x_2:
                x_1, x_2 = x_2, x_1
            if y_1 > y_2:
                y_1, y_2 = y_2, y_1
            area = (x_2 - x_1 + 1) * (y_2 - y_1 + 1)

            if exclude_overlaps:
                greens = list(pairwise(tiles + [tiles[0]]))
                for (x_3, y_3), (x_4, y_4) in greens:
                    if x_3 > x_4:
                        x_3, x_4 = x_4, x_3
                    if y_3 > y_4:
                        y_3, y_4 = y_4, y_3
                    if x_3 < x_2 and y_3 < y_2 and x_4 > x_1 and y_4 > y_1:
                        # break if green overlaps at all with rectangle
                        break
                else:
                    areas.append(area)
            else:
                areas.append(area)

    return max(areas)


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    return get_largest_area(data, exclude_overlaps=False)


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    return get_largest_area(data, exclude_overlaps=True)


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_09/input.txt")
    input_data = read_input("tests/year2025/day_09/test_input.txt")

    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
