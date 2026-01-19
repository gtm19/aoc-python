"""
Advent of Code solution for day 10.

See https://adventofcode.com/2025/day/10 for details.
"""


def read_input(file_path: str) -> list[str]:
    """Read the input file and return a list of lines."""
    with open(file_path, "r") as f:
        return f.read().splitlines()


SWITCH_POSITIONS = [".", "#"]


def process_lines(
    data: list[str],
) -> list[tuple[str, set[tuple[int, ...]], tuple[int, ...]]]:
    processed: list[tuple[str, set[tuple[int, ...]], tuple[int, ...]]] = []
    for line in data:
        light, *wiring, joltage = line.split(" ")
        processed.append(
            (
                light[1:-1],
                set(tuple(map(int, wire[1:-1].split(","))) for wire in wiring),
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
        # initial light state
        start = [0] * len(light)
        # target light state
        expected = tuple(list(light))

        # queue of light states to explore
        light_options = [(0, start)]

        while True:
            # remove the first option from the queue
            presses, current = light_options.pop(0)

            # filter wiring options that exceed joltage
            wiring_filtered = {
                w for w in wiring if all(current[i] + 1 <= joltage[i] for i in w)
            }

            # try each wiring option
            for w in wiring_filtered:
                # apply the wiring to the current state
                new = [c + (1 if i in w else 0) for i, c in enumerate(current)]
                # determine the actual light state
                actual = tuple(SWITCH_POSITIONS[i % 2] for i in new)
                # check if we reached the expected state
                if expected == actual:
                    # we're done with this machine
                    break
                # otherwise, add the new state to the queue
                light_options.append((presses + 1, new))
            else:
                continue
            # take note of the number of presses for this machine
            total += presses + 1
            # go to the next machine
            break

    return total


def part_two(data: list[str]) -> int:
    machines = process_lines(data)
    total: int = 0

    # for each machine
    for i, (light, wiring, joltage) in enumerate(machines):
        # initial light state
        start = tuple(0 for _ in light)

        # queue of light states to explore
        light_options = {(0, start)}

        while True:
            # remove the first option from the queue
            presses, current = light_options.pop()

            # filter wiring options that exceed joltage
            wiring_filtered = {
                w for w in wiring if all(current[i] + 1 <= joltage[i] for i in w)
            }

            # try each wiring option
            for w in wiring_filtered:
                # apply the wiring to the current state
                new = tuple(c + (1 if i in w else 0) for i, c in enumerate(current))
                # check if we reached the expected state
                if joltage == tuple(new):
                    # we're done with this machine
                    break
                # otherwise, add the new state to the queue
                light_options.add((presses + 1, new))
            else:
                continue
            # take note of the number of presses for this machine
            total += presses
            # go to the next machine
            break

    return total


if __name__ == "__main__":
    # input_data = read_input("solutions/year2025/day_10/input.txt")
    input_data = read_input("tests/year2025/day_10/test_input.txt")

    # print("Part 1:", part_one(input_data))
    print("Part 2:", part_two(input_data))
