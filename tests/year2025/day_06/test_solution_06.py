"""
Tests for day 6 of Advent of Code 2025.
"""

from solutions.year2025.day_06.solution import part_one, part_two, read_input

input_data = read_input("tests/year2025/day_06/test_input.txt")


def test_part_one():
    assert part_one(input_data) == 4277556


def test_part_two():
    assert part_two(input_data) == 3263827
