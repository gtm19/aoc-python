"""
Tests for day 3 of Advent of Code 2025.
"""

from solutions.year2025.day_03.solution import part_one, part_two, read_input

input_data = read_input("tests/year2025/day_03/test_input.txt")


def test_part_one():
    assert part_one(input_data) == 357


def test_part_two():
    assert part_two(input_data) == 3121910778619
