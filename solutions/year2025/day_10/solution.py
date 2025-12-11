"""
Advent of Code solution for day 10.

See https://adventofcode.com/2025/day/10 for details.
"""

from collections import defaultdict
from itertools import combinations_with_replacement


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


SWITCH_POSITIONS = [".", "#"]


def process_lines(
    data: list[str],
) -> list[tuple[str, list[tuple[int, ...]], tuple[int, ...]]]:
    processed: list[tuple[str, list[tuple[int, ...]], tuple[int, ...]]] = []
    for line in data:
        light, *wiring, joltage = line.split(" ")
        processed.append(
            (
                light[1:-1],
                [tuple(map(int, wire[1:-1].split(","))) for wire in wiring],
                tuple(map(int, joltage[1:-1].split(","))),
            ),
        )
    return processed


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    machines = process_lines(data)
    total: int = 0

    # for each machine
    for light, wiring, joltage in machines:
        n = 1
        while True:
            wiring_combos = combinations_with_replacement(wiring, n)
            for combo in wiring_combos:
                start = [0] * len(light)
                for press in combo:
                    for i in press:
                        start[i] = (start[i] + 1) % len(SWITCH_POSITIONS)
                if "".join(SWITCH_POSITIONS[i] for i in start) == light:
                    break
            else:
                n += 1
                continue
            total += n
            break

    return total


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    machines = process_lines(data)
    total: int = 0

    # for each machine
    for m_i, (light, wiring, joltage) in enumerate(machines):
        n = min(joltage)
        while True:
            wiring_combos = combinations_with_replacement(wiring, n)
            for combo in wiring_combos:
                start = defaultdict(int)
                for press in combo:
                    for i in press:
                        start[i] += 1
                if tuple(v for k, v in sorted(start.items())) == joltage:
                    break
            else:
                n += 1
                continue
            print(f"Machine {m_i + 1} requires {n} presses for joltage {joltage}")
            total += n
            break

    return total


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_10/input.txt")
    input_data = read_input("tests/year2025/day_10/test_input.txt")

    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
