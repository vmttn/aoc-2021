from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import re
from typing import List, Optional, Tuple


@dataclass
class Cell:
    value: int
    marked: bool = False


class Board:
    def __init__(self, raw: List[List[int]]):
        self.cells = [[Cell(v) for v in row] for row in raw]

    def find(self, value: int) -> Optional[Tuple[int, int]]:
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell.value == value:
                    return i, j
        return None

    def sum_unmarked(self) -> int:
        return sum(sum(c.value for c in row if not c.marked) for row in self.cells)

    def check_bingo(self, row_idx: int, col_idx: int) -> bool:
        return all([c.marked for c in self.cells[row_idx]]) or all(
            [row[col_idx].marked for row in self.cells]
        )

    def play(self, value: int) -> Optional[int]:
        coord = self.find(value)
        if coord is not None:
            i, j = coord
            self.cells[i][j].marked = True
            if self.check_bingo(i, j):
                return self.sum_unmarked()


def solve_part_one(boards: List[Board], drawn_numbers: List[int]) -> Tuple[int, int]:
    for draw in drawn_numbers:
        scores = []
        for board in boards:
            score = board.play(draw)
            if score is not None:
                scores.append(score)
        if len(scores) > 0:
            return draw, max(scores)

    return -1, -1


def solve_part_two(boards: List[Board], drawn_numbers: List[int]) -> Tuple[int, int]:
    for draw in drawn_numbers:
        scores: List[Tuple[int, Board]] = []
        for board in boards:
            score = board.play(draw)
            if score is not None:
                scores.append((score, board))
        for score, board in scores:
            boards = [b for b in boards if b != board]
        if len(boards) == 0:
            return draw, min([s for s, _ in scores])
    return -1, -1


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        drawn_numbers = [int(s) for s in input_file.readline().rstrip("\n").split(",")]

        raw_boards = []
        for line in input_file:
            if line == "\n":
                raw_boards.append([])
            else:

                raw_boards[-1].append([int(s) for s in re.findall(r"\d+", line)])
        boards = [Board(data) for data in raw_boards]

        winning_number, unmarked_numbers_sum = solve_part_one(boards, drawn_numbers)
        print(f"part one: {winning_number * unmarked_numbers_sum}")

        winning_number, unmarked_numbers_sum = solve_part_two(boards, drawn_numbers)
        print(f"part two: {winning_number * unmarked_numbers_sum}")
