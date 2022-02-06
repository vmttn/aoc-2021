from typing import List

import pytest

from day_3 import solver


@pytest.fixture
def planned_course() -> List[int]:
    return [
        int("00100", 2),
        int("11110", 2),
        int("10110", 2),
        int("10111", 2),
        int("10101", 2),
        int("01111", 2),
        int("00111", 2),
        int("11100", 2),
        int("10000", 2),
        int("11001", 2),
        int("00010", 2),
        int("01010", 2),
    ]


def test_part_one(planned_course: List[int]):
    gamma_rate, espilon_rate = solver.solve_part_one(planned_course, word_length=5)
    assert gamma_rate == 22
    assert espilon_rate == 9


def test_part_two(planned_course: List[int]):
    oxygen_generator_rating, co2_scrubber_rating = solver.solve_part_two(
        planned_course, word_length=5
    )
    assert oxygen_generator_rating == 23
    assert co2_scrubber_rating == 10
