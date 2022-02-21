from typing import List

import pytest

from day_12 import solver

CAVE_SYSTEMS = {
    "first": [
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ],
    "slightly_larger": [
        "dc-end",
        "HN-start",
        "start-kj",
        "dc-start",
        "dc-HN",
        "LN-dc",
        "HN-end",
        "kj-sa",
        "kj-HN",
        "kj-dc",
    ],
    "even_larger": [
        "fs-end",
        "he-DX",
        "fs-he",
        "start-DX",
        "pj-DX",
        "end-zg",
        "zg-sl",
        "zg-pj",
        "pj-he",
        "RW-he",
        "fs-DX",
        "pj-RW",
        "zg-RW",
        "start-pj",
        "he-WI",
        "zg-he",
        "pj-fs",
        "start-RW",
    ],
}


@pytest.mark.parametrize(
    "cave_system, path_count",
    [
        (
            CAVE_SYSTEMS["first"],
            10,
        ),
        (
            CAVE_SYSTEMS["slightly_larger"],
            19,
        ),
        (
            CAVE_SYSTEMS["even_larger"],
            226,
        ),
    ],
)
def test_part_one(cave_system: List[str], path_count: int):
    assert solver.solve_part_one(cave_system=cave_system) == path_count


@pytest.mark.parametrize(
    "cave_system, path_count",
    [
        (
            CAVE_SYSTEMS["first"],
            36,
        ),
        (
            CAVE_SYSTEMS["slightly_larger"],
            103,
        ),
        (
            CAVE_SYSTEMS["even_larger"],
            3509,
        ),
    ],
)
def test_part_two(cave_system: List[str], path_count: int):
    assert solver.solve_part_two(cave_system=cave_system) == path_count
