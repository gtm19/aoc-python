"""
Tests for day 7 of Advent of Code 2025.
"""

from solutions.year2025.day_07.solution import part_one, part_two, read_input

input_data = read_input("tests/year2025/day_07/test_input.txt")


def test_part_one():
    assert part_one(input_data) == 21


def test_part_two():
    assert part_two(input_data) == 40
