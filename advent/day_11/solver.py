from copy import deepcopy
from itertools import count
from pathlib import Path
from typing import List


def flash(octopuses_grid: List[List[int]], i: int, j: int):
    if i < 0 or i > len(octopuses_grid) - 1 or j < 0 or j > len(octopuses_grid[i]) - 1:
        return

    octopuses_grid[i][j] += 1
    if octopuses_grid[i][j] >= 10:
        octopuses_grid[i][j] = -1000
        flash(octopuses_grid, i - 1, j - 1)
        flash(octopuses_grid, i - 1, j)
        flash(octopuses_grid, i - 1, j + 1)
        flash(octopuses_grid, i, j + 1)
        flash(octopuses_grid, i + 1, j + 1)
        flash(octopuses_grid, i + 1, j)
        flash(octopuses_grid, i + 1, j - 1)
        flash(octopuses_grid, i, j - 1)


def step(octopuses_grid: List[List[int]]) -> int:
    flash_count = 0

    for i in range(len(octopuses_grid)):
        for j in range(len(octopuses_grid[i])):
            octopuses_grid[i][j] += 1

    for i in range(len(octopuses_grid)):
        for j in range(len(octopuses_grid[i])):
            if octopuses_grid[i][j] >= 10:
                flash(octopuses_grid, i, j)

    for i in range(len(octopuses_grid)):
        for j in range(len(octopuses_grid[i])):
            if octopuses_grid[i][j] < 0:
                flash_count += 1
                octopuses_grid[i][j] = 0

    return flash_count


def solve_part_one(octopuses_grid: List[List[int]]) -> int:
    return sum(step(octopuses_grid=octopuses_grid) for s in range(100))


def solve_part_two(octopuses_grid: List[List[int]]) -> int:
    return next(
        s
        for s in count(1)
        if step(octopuses_grid=octopuses_grid)
        == len(octopuses_grid) * len(octopuses_grid[0])
    )


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        octopuses_grid = [list(map(int, line.strip("\n"))) for line in input_file]

        ret = solve_part_one(octopuses_grid=deepcopy(octopuses_grid))
        print(f"part one: {ret}")

        ret = solve_part_two(octopuses_grid=deepcopy(octopuses_grid))
        print(f"part two: {ret}")
