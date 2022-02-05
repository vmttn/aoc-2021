from typing import List

import pytest

from day_2 import solver
from day_2.solver import Command, Direction


@pytest.fixture
def planned_course() -> List[Command]:
    return [
        Command(Direction.FORWARD, 5),
        Command(Direction.DOWN, 5),
        Command(Direction.FORWARD, 8),
        Command(Direction.UP, 3),
        Command(Direction.DOWN, 8),
        Command(Direction.FORWARD, 2),
    ]


def test_part_one(planned_course: List[Command]):
    p = solver.solve_part_one(planned_course)
    assert p.x == 15
    assert p.y == 10
    assert p.x * p.y == 150


def test_part_two(planned_course: List[Command]):
    p = solver.solve_part_two(planned_course)
    assert p.x == 15
    assert p.y == 60
    assert p.x * p.y == 900
