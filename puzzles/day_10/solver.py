from audioop import reverse
from dataclasses import dataclass
from pathlib import Path
from typing import List


COST_BY_ILLEGAL_CHAR = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

COST_BY_MISSING_CHAR = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

CLOSE_CHAR_BY_OPEN_CHAR = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def corrupted_score(line) -> int:
    stack = []
    for c in line:
        if c in CLOSE_CHAR_BY_OPEN_CHAR:
            stack.append(CLOSE_CHAR_BY_OPEN_CHAR[c])
        else:
            expected = stack.pop()
            if c != expected:
                return COST_BY_ILLEGAL_CHAR[c]
    return 0


def incomplete_score(line) -> int:
    stack = []
    for c in line:
        if c in CLOSE_CHAR_BY_OPEN_CHAR:
            stack.append(CLOSE_CHAR_BY_OPEN_CHAR[c])
        else:
            stack.pop()

    score = 0
    for c in reversed(stack):
        score *= 5
        score += COST_BY_MISSING_CHAR[c]

    return score


def solve_part_one(navigation_subsystem: List[str]) -> int:
    return sum(corrupted_score(line) for line in navigation_subsystem)


def solve_part_two(navigation_subsystem: List[str]) -> int:
    incomplete_lines = list(
        filter(lambda x: corrupted_score(x) == 0, navigation_subsystem)
    )

    return sorted([incomplete_score(line) for line in incomplete_lines])[
        len(incomplete_lines) // 2
    ]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        navigation_subsystem = [line.strip("\n") for line in input_file]

        ret = solve_part_one(navigation_subsystem=navigation_subsystem)
        print(f"part one: {ret}")

        ret = solve_part_two(navigation_subsystem=navigation_subsystem)
        print(f"part two: {ret}")
