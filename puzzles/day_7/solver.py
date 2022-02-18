from pathlib import Path
from typing import List, Tuple
from statistics import median
import sys


def solve_part_one(horizontal_positions: List[int]) -> Tuple[int, int]:
    target_position = int(median(horizontal_positions))
    fuel = sum(map(lambda p: abs(target_position - p), horizontal_positions))
    return target_position, fuel


def solve_part_two(horizontal_positions: List[int]) -> Tuple[int, int]:
    target_position, least_cost = -1, sys.maxsize
    for x in range(min(horizontal_positions), max(horizontal_positions) + 1):
        cost = sum(
            map(
                lambda d: d * (d + 1) // 2,
                map(lambda p: abs(x - p), horizontal_positions),
            )
        )
        if cost < least_cost:
            target_position, least_cost = x, cost
    return target_position, least_cost


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        horizontal_positions = list(map(int, input_file.readline().split(",")))

        _, least_fuel = solve_part_one(horizontal_positions)
        print(f"part one: {least_fuel}")

        _, least_fuel = solve_part_two(horizontal_positions)
        print(f"part two: {least_fuel}")
