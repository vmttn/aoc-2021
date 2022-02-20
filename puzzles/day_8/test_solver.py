from pathlib import Path
from typing import List

import pytest

from day_8 import solver
from day_8.solver import Entry


@pytest.fixture
def notes() -> List[Entry]:
    input_path = Path(__file__).parent / "test_input"
    with input_path.open("r") as input_file:
        entries = [
            Entry(*list(map(lambda s: s.strip().split(" "), line.split("|"))))
            for line in input_file
        ]
    return entries


def test_part_one(notes: List[Entry]):
    assert solver.solve_part_one(notes=notes) == 26


def test_part_two_second_example(notes: List[Entry]):
    assert solver.solve_part_two(notes=notes) == 61229


def test_part_two_first_example():
    assert (
        solver.solve_part_two(
            notes=[
                Entry(
                    patterns=[
                        "acedgfb",
                        "cdfbe",
                        "gcdfa",
                        "fbcad",
                        "dab",
                        "cefabd",
                        "cdfgeb",
                        "eafb",
                        "cagedb",
                        "ab",
                    ],
                    digits=["cdfeb", "fcadb", "cdfeb", "cdbaf"],
                )
            ]
        )
        == 5353
    )
