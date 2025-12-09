"""
Advent of Code solution for day 8.

See https://adventofcode.com/2025/day/8 for details.
"""

from math import prod, sqrt


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


def process_junction_boxes(data: list[str], n: int = 1000) -> tuple[int, int]:
    coords = [tuple(map(int, v.split(","))) for v in data]

    # make distance dict
    d: dict[tuple[int, int], float] = {}
    for i, x in enumerate(coords):
        for j, y in enumerate(coords):
            if i >= j:
                continue
            d[(i, j)] = sqrt(sum((x_v - y_v) ** 2 for x_v, y_v in zip(x, y)))

    # sort top n keys by values to get n closest pairs
    top_n = sorted(d.items(), key=lambda x: x[1])

    # make a list of sets of nodes, each initially of size 1
    circuits = [{i} for i in range(len(coords))]

    for t, ((i, j), _) in enumerate(top_n):
        # find the sets that contain i and j
        set_i = next(s for s in circuits if i in s)
        set_j = next(s for s in circuits if j in s)

        # if they are different sets, merge them
        if set_i is not set_j:
            set_i.update(set_j)
            circuits.remove(set_j)
        if t == n:
            top = prod(sorted(len(c) for c in circuits)[-3:])
        if len(set_i) == len(coords):
            x_1 = coords[i][0]
            x_2 = coords[j][0]
            wall_dist = x_1 * x_2
            break

    return top, wall_dist


def part_one(data: list[str]) -> int:
    """Solve part one of the day's challenge."""
    top_n, _ = process_junction_boxes(data)
    return top_n


def part_two(data: list[str]) -> int:
    """Solve part two of the day's challenge."""
    _, wall_dist = process_junction_boxes(data)
    return wall_dist


if __name__ == "__main__":
    input_data = read_input("solutions/year2025/day_08/input.txt")
    # input_data = read_input("tests/year2025/day_08/test_input.txt")

    print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
