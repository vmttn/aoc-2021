import functools
import logging
from pathlib import Path
import time
from typing import List
from collections import Counter, defaultdict


logging.basicConfig()
logger = logging.getLogger()


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        res = func(*args, **kwargs)
        logger.debug(time.perf_counter() - tic)
        return res

    return wrapper


class School:
    def __init__(self, initial_school: List[int]):
        self.school = defaultdict(lambda: 0)
        self.school.update(dict(Counter(initial_school)))

    def forward(self):
        birthing = self.school[0]
        for i in range(9):
            self.school[i] = self.school[i + 1]
        self.school[6] += birthing
        self.school[8] = birthing

    def forward_n_days(self, n: int):
        for _ in range(n):
            self.forward()

    def count(self):
        return sum(self.school.values())


@timer
def solve(initial_school: List[int], day: int) -> int:
    school = School(initial_school)
    school.forward_n_days(day)
    return school.count()


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        initial_school = list(map(int, input_file.readline().split(",")))
        lanternfish_count = solve(initial_school, 80)
        print(f"part one: {lanternfish_count}")
        lanternfish_count = solve(initial_school, 256)
        print(f"part two: {lanternfish_count}")
