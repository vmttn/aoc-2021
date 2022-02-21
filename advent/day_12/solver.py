from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict, Counter


def solve_part_one(cave_system: List[str]) -> int:
    graph = defaultdict(set)
    for line in cave_system:
        a, b = line.split("-")
        graph[a] |= set([b])
        graph[b] |= set([a])

    def walk(path: List[str], graph: Dict[str, Set[str]]) -> List[List[str]]:
        if path[-1] == "end":
            return [path]

        paths = []
        for neighbor in graph[path[-1]]:
            if neighbor.isupper() or neighbor not in path:
                paths = [*paths, *walk([*path, neighbor], graph)]

        return paths

    paths = walk(["start"], graph)
    return len(paths)


def solve_part_two(cave_system: List[str]) -> int:
    graph = defaultdict(set)
    for line in cave_system:
        a, b = line.split("-")
        graph[a] |= set([b])
        graph[b] |= set([a])

    def walk(path: List[str], graph: Dict[str, Set[str]]) -> List[List[str]]:
        if path[-1] == "end":
            return [path]

        paths = []
        for neighbor in graph[path[-1]]:
            if neighbor == "start":
                continue

            if (
                neighbor.isupper()
                or neighbor not in path
                or 2 not in Counter(filter(str.islower, path)).values()
            ):
                paths = [*paths, *walk([*path, neighbor], graph)]

        return paths

    paths = walk(["start"], graph)
    return len(paths)


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        cave_system = [line.strip("\n") for line in input_file]

        ret = solve_part_one(cave_system=cave_system)
        print(f"part one: {ret}")

        ret = solve_part_two(cave_system=cave_system)
        print(f"part two: {ret}")
