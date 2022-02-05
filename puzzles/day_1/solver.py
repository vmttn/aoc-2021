from pathlib import Path
from typing import List


def solve_part_one(report: List[int]) -> int:
    return [report[i] - report[i - 1] > 0 for i in range(1, len(report))].count(True)


def solve_part_two(report: List[int]) -> int:
    return solve_part_one(
        [report[i - 2] + report[i - 1] + report[i] for i in range(2, len(report))]
    )


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        report = [int(line) for line in input_file]
        print(f"part one: {solve_part_one(report)}")
        print(f"part two: {solve_part_two(report)}")
