from typing import List, Tuple

import pytest

from day_14 import solver


@pytest.fixture
def polymer_template() -> str:
    return "NNCB"


@pytest.fixture
def insertion_rules() -> List[Tuple[str, str]]:
    return [
        ("CH", "B"),
        ("HH", "N"),
        ("CB", "H"),
        ("NH", "C"),
        ("HB", "C"),
        ("HC", "B"),
        ("HN", "C"),
        ("NN", "C"),
        ("BH", "H"),
        ("NC", "B"),
        ("NB", "B"),
        ("BN", "B"),
        ("BB", "N"),
        ("BC", "B"),
        ("CC", "N"),
        ("CN", "C"),
    ]


def test_part_one(polymer_template, insertion_rules):
    assert (
        solver.solve_part_one(
            polymer_template=polymer_template,
            insertion_rules=insertion_rules,
        )
        == 1588
    )


def test_part_two(polymer_template, insertion_rules):
    assert (
        solver.solve_part_two(
            polymer_template=polymer_template,
            insertion_rules=insertion_rules,
        )
        == 2188189693529
    )
