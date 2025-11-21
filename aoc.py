from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

SOLUTIONS_DIR = Path(__file__).parent / "solutions"
TESTS_DIR = Path(__file__).parent / "tests"
TEMPLATES_DIR = Path(__file__).parent / "templates"


def setup(year: int | None = None, day_number: int | None = None) -> None:
    """Set up a new Advent of Code solution for the given year and day number."""
    year = year or datetime.now().year
    day_number = day_number or datetime.now().day

    # Define paths
    day_dir = SOLUTIONS_DIR / f"year{year}" / f"day_{day_number:02}"
    day_dir.mkdir(parents=True, exist_ok=True)
    day_file = day_dir / "solution.py"
    input_file = day_dir / "input.txt"

    day_test_dir = TESTS_DIR / f"year{year}" / f"day_{day_number:02}"
    day_test_dir.mkdir(parents=True, exist_ok=True)
    day_test_file = day_test_dir / "test_solution.py"
    input_test_file = day_test_dir / "test_input.txt"

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    solution_template = env.get_template("day_00.py.jinja")
    test_template = env.get_template("test_day_00.py.jinja")

    # context
    context = {"year": year, "day_number": day_number}

    # Render and write solution file
    with day_file.open("w") as f:
        f.write(solution_template.render(context))
    # Create empty input file
    input_file.touch()

    # Render and write test file
    with day_test_file.open("w") as f:
        f.write(test_template.render(context))
    # Create empty test input file
    input_test_file.touch()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Set up a new Advent of Code solution."
    )
    parser.add_argument(  # pyright: ignore[reportUnusedCallResult]
        "--year",
        type=int,
        help="The year of the Advent of Code challenge.",
        default=None,
    )
    parser.add_argument(  # pyright: ignore[reportUnusedCallResult]
        "--day",
        type=int,
        help="The day number of the Advent of Code challenge.",
        default=None,
    )
    args = parser.parse_args()
    setup(year=args.year, day_number=args.day)  # pyright: ignore[reportAny]
