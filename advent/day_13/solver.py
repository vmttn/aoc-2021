from itertools import takewhile
import logging
from pathlib import Path
from typing import List, Tuple


logging.basicConfig()
logger = logging.getLogger()


class Paper:
    def __init__(self, dots: List[Tuple[int, int]]) -> None:
        self.dots = set(dots)
        self.width = max([x for x, _ in self.dots]) + 1
        self.height = max([y for _, y in self.dots]) + 1

    def __str__(self) -> str:
        return "\n".join(
            "".join(["#" if (x, y) in self.dots else "." for x in range(self.width)])
            for y in range(self.height)
        )

    def fold(self, instruction: str):
        axis, line = instruction.split("=")[0][-1], int(instruction.split("=")[1])

        def projection(x: int, y: int) -> Tuple[int, int]:
            if axis == "x":
                return line - abs(x - line), y
            else:
                return x, line - abs(y - line)

        def is_on_line(x: int, y: int) -> bool:
            return x == line if axis == "x" else y == line

        self.dots = {projection(*dot) for dot in self.dots}
        self.dots = {dot for dot in self.dots if not is_on_line(*dot)}

        if axis == "x":
            self.width //= 2
        else:
            self.height //= 2


def solve_part_one(dots: List[Tuple[int, int]], fold_instructions: List[str]) -> int:
    paper = Paper(dots=dots)

    logger.debug(f"STEP 0\n{paper}".center(paper.width, "="))

    for step, instruction in enumerate(fold_instructions):
        paper.fold(instruction)
        logger.debug(f"STEP {step}\n{paper}".center(paper.width, "="))

    return len(paper.dots)


def solve_part_two(dots: List[Tuple[int, int]], fold_instructions: List[str]) -> Paper:
    paper = Paper(dots=dots)

    for instruction in fold_instructions:
        paper.fold(instruction)

    return paper


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        dots = [
            tuple(map(int, l.split(",")))
            for l in takewhile(lambda l: l != "\n", input_file)
        ]

        fold_instructions = [l.strip("\n") for l in input_file]

        ret = solve_part_one(dots=dots, fold_instructions=fold_instructions[:1])
        print(f"part one: {ret}")

        ret = solve_part_two(dots=dots, fold_instructions=fold_instructions)
        print(f"part two:\n{ret}")
