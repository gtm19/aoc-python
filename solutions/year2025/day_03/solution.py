"""
Advent of Code solution for day 3.

See https://adventofcode.com/2025/day/3 for details.
"""


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


def get_joltage(bank: str, n: int = 2) -> int:
    """Get the joltage from the bank string by selecting n highest digits in order."""
    digits: list[tuple[int, str]] = []
    left: int = 0
    right: int = len(bank) - n + 1

    for _ in range(n):
        if digits:
            left = digits[-1][0] + 1
            right += 1
        digit: str = max(bank[left:right])
        digit_pos: int = bank[left:right].index(digit) + left
        digits.append((digit_pos, digit))

    return int("".join(d for _, d in digits))


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    return sum(get_joltage(bank) for bank in data)


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    return sum(get_joltage(bank, n=12) for bank in data)


if __name__ == "__main__":
    input_data: list[str] = read_input("solutions/year2025/day_03/input.txt")
    p1: int = part_one(input_data)
    print("Part 1:", p1)
    p2: int = part_two(data=input_data)
    print("Part 2:", p2)
