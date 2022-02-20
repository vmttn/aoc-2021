from typing import List

import pytest

from day_06 import solver


@pytest.fixture
def lanternfish_school() -> List[int]:
    return [3, 4, 3, 1, 2]


def test_solve(lanternfish_school: List[int]):
    expected_counts = [
        5,
        5,
        6,
        7,
        9,
        10,
        10,
        10,
        10,
        11,
        12,
        15,
        17,
        19,
        20,
        20,
        21,
        22,
        26,
    ]

    for day, expected_count in enumerate(expected_counts):
        assert solver.solve(lanternfish_school, day) == expected_count
