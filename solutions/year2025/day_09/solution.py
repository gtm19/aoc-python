"""
Advent of Code solution for day 9.

See https://adventofcode.com/2025/day/9 for details.
"""


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    tiles = list(tuple(map(int, d.split(","))) for d in data)
    areas = []
    for i in range(len(tiles)):
        for j in range(i):
            t_1 = tiles[i]
            t_2 = tiles[j]
            area = (abs(t_1[0] - t_2[0]) + 1) * (abs(t_1[1] - t_2[1]) + 1)
            areas.append(area)
    return max(areas)


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    return -9999


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_09/input.txt")
    # input_data = read_input("tests/year2025/day_09/test_input.txt")

    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
