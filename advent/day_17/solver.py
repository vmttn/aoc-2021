from pathlib import Path
import re
from typing import Tuple

Area = Tuple[Tuple[int, int], Tuple[int, int]]


def solve_part_one(target_area: Area) -> int:
    highest = 0
    for vx0 in range(1, 100):
        for vy0 in range(0, 100):
            current_highest = 0
            x, y = 0, 0
            vx, vy = vx0, vy0
            while True:
                x, y = x + vx, y + vy
                current_highest = max(current_highest, y)
                if x > target_area[0][1] or y < target_area[1][0]:
                    break
                elif x > target_area[0][0] and y < target_area[1][1]:
                    highest = max(highest, current_highest)
                    break
                vx, vy = max(vx - 1, 0), vy - 1
    return highest


def solve_part_two(target_area: Area) -> int:
    count = 0
    for vx0 in range(1, 315):
        for vy0 in range(-100, 200):
            x, y = 0, 0
            vx, vy = vx0, vy0
            while True:
                x, y = x + vx, y + vy
                if x > target_area[0][1] or y < target_area[1][0]:
                    break
                elif x >= target_area[0][0] and y <= target_area[1][1]:
                    count += 1
                    break
                vx, vy = max(vx - 1, 0), vy - 1
    return count


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        values = list(map(int, re.findall(r"-?\d+", input_file.readline())))
        target_area = ((values[0], values[1]), (values[2], values[3]))

        ret = solve_part_one(target_area=target_area)
        print(f"part one: {ret}")

        ret = solve_part_two(target_area=target_area)
        print(f"part two: {ret}")
