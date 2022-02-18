from typing import List

import pytest

from day_7 import solver


@pytest.fixture
def horizontal_positions() -> List[int]:
    return [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_part_one(horizontal_positions: List[int]):
    position, fuel = solver.solve_part_one(horizontal_positions)
    assert position == 2
    assert fuel == 37


def test_part_two(horizontal_positions: List[int]):
    position, fuel = solver.solve_part_two(horizontal_positions)
    assert position == 5
    assert fuel == 168
