from typing import List

import pytest

from day_10 import solver


@pytest.fixture
def navigation_subsystem() -> List[str]:
    return [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]",
    ]


def test_part_one(navigation_subsystem: List[str]):
    assert solver.solve_part_one(navigation_subsystem=navigation_subsystem) == 26397
