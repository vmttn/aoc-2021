from typing import List

import pytest

from day_1 import solver


@pytest.fixture
def report():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part_one(report: List[int]):
    assert solver.solve_part_one(report) == 7


def test_part_two(report: List[int]):
    assert solver.solve_part_two(report) == 5
