from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable, List, Mapping


class Direction(str, Enum):
    FORWARD = "FORWARD"
    DOWN = "DOWN"
    UP = "UP"


@dataclass(frozen=True)
class Command:
    direction: Direction
    value: int

    @classmethod
    def from_str(cls, v: str) -> Command:
        return Command(Direction[v.split(" ")[0].upper()], int(v.split(" ")[1]))


@dataclass(frozen=True)
class Position:
    x: int
    y: int


def solve_part_one(planned_course: List[Command]) -> Position:
    position = Position(0, 0)

    COMMAND_HANDLERS: Mapping[Direction, Callable[[Position, int], Position]] = {
        Direction.FORWARD: lambda p, v: Position(p.x + v, p.y),
        Direction.DOWN: lambda p, v: Position(p.x, p.y + v),
        Direction.UP: lambda p, v: Position(p.x, p.y - v),
    }

    for command in planned_course:
        position = COMMAND_HANDLERS[command.direction](position, command.value)
    return position


@dataclass(frozen=True)
class Status:
    position: Position
    aim: int


def solve_part_two(planned_course: List[Command]) -> Position:
    status = Status(position=Position(0, 0), aim=0)

    COMMAND_HANDLERS: Mapping[Direction, Callable[[Status, int], Status]] = {
        Direction.FORWARD: lambda s, v: Status(
            Position(s.position.x + v, s.position.y + s.aim * v), s.aim
        ),
        Direction.DOWN: lambda s, v: Status(s.position, s.aim + v),
        Direction.UP: lambda s, v: Status(s.position, s.aim - v),
    }

    for command in planned_course:
        status = COMMAND_HANDLERS[command.direction](status, command.value)
    return status.position


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        planned_course = [Command.from_str(line) for line in input_file]

        position = solve_part_one(planned_course)
        print(f"part one: {position.x * position.y}")

        position = solve_part_two(planned_course)
        print(f"part two: {position.x * position.y}")
