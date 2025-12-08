"""
Advent of Code solution for day 7.

See https://adventofcode.com/2025/day/7 for details.
"""


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


def make_grid(data: list[str]) -> dict[complex, str]:
    return {complex(x, y): c for x, row in enumerate(data) for y, c in enumerate(row)}


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    grid = make_grid(data)
    beams = set(k for k, v in grid.items() if v == "S")
    splits = 0
    for i in range(1, len(data)):
        for beam in list(beams):
            beams.remove(beam)
            new_beam = beam + 1
            if grid.get(new_beam) == "^":
                beams.update((new_beam + 1j, new_beam - 1j))
                splits += 1
            else:
                beams.add(new_beam)
    return splits


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    return -9999


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_07/input.txt")
    # input_data = read_input("tests/year2025/day_07/test_input.txt")

    print(input_data)

    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
