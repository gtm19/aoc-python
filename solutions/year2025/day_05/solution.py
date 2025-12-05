"""
Advent of Code solution for day 5.

See https://adventofcode.com/2025/day/5 for details.
"""


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


def ranges_and_ingredients(data: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ingredients = []
    for d in data:
        if "-" in d:
            left, right = map(int, d.split("-"))
            ranges.append((left, right))
        elif d == "":
            continue
        else:
            ingredients.append(int(d))
    return ranges, ingredients


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    ranges, ingredients = ranges_and_ingredients(data)
    fresh = 0
    for i in ingredients:
        for left, right in ranges:
            if left <= i <= right:
                fresh += 1
                break
    return fresh


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    ranges, _ = ranges_and_ingredients(data)
    ranges.sort()
    new_ranges = [ranges.pop(0)]

    for left, right in ranges:
        if left > new_ranges[-1][1]:
            new_ranges.append((left, right))
        else:
            # extend last range to the right
            new_ranges[-1] = (new_ranges[-1][0], max(new_ranges[-1][1], right))

    return sum(right - left + 1 for left, right in new_ranges)


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_05/input.txt")
    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
