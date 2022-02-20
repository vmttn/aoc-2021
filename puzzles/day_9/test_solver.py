from typing import List

import pytest

from day_9 import solver


@pytest.fixture
def height_map() -> List[List[int]]:
    return [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_part_one(height_map: List[List[int]]):
    assert solver.solve_part_one(height_map=height_map) == 15


def test_part_two(height_map: List[List[int]]):
    assert solver.solve_part_two(height_map=height_map) == 1134
