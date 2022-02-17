from pathlib import Path
import re
from typing import List, Tuple

Line = Tuple[Tuple[int, int], Tuple[int, int]]


class Diagram:
    def __init__(self, lines: List[Line]):
        self.cells = [[0] * (max(max(l[1][1], l[0][1]) for l in lines) + 1)] * (
            max(max(l[1][0], l[0][0]) for l in lines) + 1
        )
        self.cells = [
            [0] * (max(max(l[1][1], l[0][1]) for l in lines) + 1)
            for _ in range(max(max(l[1][0], l[0][0]) for l in lines) + 2)
        ]
        self.fill(lines)

    def __str__(self) -> str:
        return "\n".join(
            [
                "".join([f"{'.' if cell == 0 else cell}" for cell in row])
                for row in self.cells
            ]
        )

    def fill(self, lines: List[Line]) -> None:
        for ((x0, y0), (x1, y1)) in lines:
            step = (
                abs(x1 - x0) // (x1 - x0) if x0 != x1 else 0,
                abs(y1 - y0) // (y1 - y0) if y0 != y1 else 0,
            )
            curr = (x0, y0)
            while True:
                self.cells[curr[0]][curr[1]] += 1
                if curr == (x1, y1):
                    break
                curr = (curr[0] + step[0], curr[1] + step[1])

    def get_number_of_overlaps(self) -> int:
        count = 0
        for row in self.cells:
            for cell in row:
                if cell > 1:
                    count += 1
        return count


def solve_part_one(lines: List[Line]) -> int:
    lines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]
    diagram = Diagram(lines=lines)
    return diagram.get_number_of_overlaps()


def solve_part_two(lines: List[Line]) -> int:
    diagram = Diagram(lines=lines)
    return diagram.get_number_of_overlaps()


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        lines = [
            ((int(x1), int(y1)), (int(x2), int(y2)))
            for x1, y1, x2, y2 in [re.findall(r"\d+", l) for l in input_file]
        ]
        overlap_count = solve_part_one(lines)
        print(f"part one: {overlap_count}")

        overlap_count = solve_part_two(lines)
        print(f"part two: {overlap_count}")
