"""
Advent of Code solution for day 4.

See https://adventofcode.com/2025/day/4 for details.
"""

ADJACENTS = [
    (-1, -1),
    (1, -1),
    (-1, 1),
    (1, 1),
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


def make_grid(data: list[str]) -> dict[tuple[int, int], str]:
    """Turn input into a grid-as-a-dict"""
    return {(x, y): v for y, row in enumerate(data) for x, v in enumerate(row)}


def grid_remove(
    grid: dict[tuple[int, int], str],
) -> tuple[int, dict[tuple[int, int], str]]:
    accessible: list[tuple[int, int]] = []

    for (x, y), v in grid.items():
        if v != "@":
            continue
        adjacent_rolls: int = 0
        for x_d, y_d in ADJACENTS:
            adjacent = (x + x_d, y + y_d)
            if grid.get(adjacent) == "@":
                adjacent_rolls += 1
            if adjacent_rolls >= 4:
                break
        else:
            accessible.append((x, y))

    for roll in accessible:
        grid[roll] = "."

    return len(accessible), grid


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    grid = make_grid(data)
    rolls, _ = grid_remove(grid)
    return rolls


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    grid = make_grid(data)
    total = 0

    while True:
        rolls, grid = grid_remove(grid)
        if rolls == 0:
            break
        total += rolls

    return total


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_04/input.txt")
    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
