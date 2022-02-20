from functools import reduce
from pathlib import Path
from typing import List, Tuple


def compute_local_minimums(height_map: List[List[int]]) -> List[Tuple[int, int]]:
    local_minimums = []

    for i in range(len(height_map)):
        for j in range(len(height_map[i])):
            is_local_minimum = True
            # top
            is_local_minimum &= i == 0 or height_map[i][j] < height_map[i - 1][j]
            # down
            is_local_minimum &= (
                i == len(height_map) - 1 or height_map[i][j] < height_map[i + 1][j]
            )
            # left
            is_local_minimum &= j == 0 or height_map[i][j] < height_map[i][j - 1]
            # right
            is_local_minimum &= (
                j == len(height_map[i]) - 1 or height_map[i][j] < height_map[i][j + 1]
            )

            if is_local_minimum:
                local_minimums.append((i, j))

    return local_minimums


def solve_part_one(height_map: List[List[int]]) -> int:
    return sum(height_map[i][j] + 1 for i, j in compute_local_minimums(height_map))


def scan(
    height_map: List[List[int]],
    location: Tuple[int, int],
    basin: List[Tuple[int, int]],
):
    i, j = location
    if location in basin or height_map[i][j] == 9:
        return

    basin.append(location)
    # top
    if i > 0:
        scan(height_map=height_map, location=(i - 1, j), basin=basin)
    # down
    if i < len(height_map) - 1:
        scan(height_map=height_map, location=(i + 1, j), basin=basin)
    # left
    if j > 0:
        scan(height_map=height_map, location=(i, j - 1), basin=basin)
    # right
    if j < len(height_map[i]) - 1:
        scan(height_map=height_map, location=(i, j + 1), basin=basin)


def solve_part_two(height_map: List[List[int]]) -> int:
    local_minimums = compute_local_minimums(height_map)
    basin_sizes = []

    for p, q in local_minimums:
        basin = []
        scan(height_map=height_map, location=(p, q), basin=basin)
        basin_sizes.append(len(basin))

    return reduce(lambda x, y: x * y, sorted(basin_sizes, reverse=True)[:3])


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        height_map = [list(map(int, line.strip("\n"))) for line in input_file]
        ret = solve_part_one(height_map=height_map)
        print(f"part one: {ret}")

        ret = solve_part_two(height_map=height_map)
        print(f"part two: {ret}")
