from typing import List, Tuple

import pytest

from day_13 import solver


@pytest.fixture
def dots() -> List[Tuple[int, int]]:
    return [
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    ]


@pytest.fixture
def fold_instructions() -> List[str]:
    return [
        "fold along y=7",
        "fold along x=5",
    ]


def test_part_one(dots: List[Tuple[int, int]], fold_instructions: List[str]):
    assert (
        solver.solve_part_one(dots=dots, fold_instructions=fold_instructions[:1]) == 17
    )
