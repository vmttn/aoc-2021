import heapq
from pathlib import Path
from typing import List, Tuple


def solve_part_one(risk_level_map: List[List[int]]) -> int:
    # Using dijkstra

    N = len(risk_level_map)
    heap = [(0, (0, 0))]
    seen = {(0, 0)}

    def neighbors(i: int, j: int) -> List[Tuple[int, int]]:
        return list(
            filter(
                lambda p: 0 <= p[0] <= N - 1 and 0 <= p[1] <= N - 1,
                [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)],
            )
        )

    while heap:
        risk, position = heapq.heappop(heap)

        if position == (N - 1, N - 1):
            return risk

        for neighbor in filter(lambda p: p not in seen, neighbors(*position)):
            seen.add(neighbor)
            heapq.heappush(
                heap, (risk + risk_level_map[neighbor[0]][neighbor[1]], neighbor)
            )


def repeat_map(map: List[List[int]]) -> List[List[int]]:
    N = len(map)
    return [
        [
            (
                (map[i % N][j % N] + i // N + j // N)
                + (map[i % N][j % N] + i // N + j // N) // 10
            )
            % 10
            for j in range(5 * N)
        ]
        for i in range(5 * N)
    ]


def solve_part_two(risk_level_map: List[List[int]]) -> int:
    return solve_part_one(risk_level_map=repeat_map(risk_level_map))


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        risk_level_map = [list(map(int, line.strip("\n"))) for line in input_file]

        ret = solve_part_one(risk_level_map=risk_level_map)
        print(f"part one: {ret}")

        ret = solve_part_two(risk_level_map=risk_level_map)
        print(f"part two: {ret}")
