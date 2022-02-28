from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum
from functools import reduce
from itertools import chain
from pathlib import Path
from typing import List, Optional


class PacketType(int, Enum):
    SUM = 0
    MULT = 1
    MIN = 2
    MAX = 3
    LIT = 4
    GT = 5
    LT = 6
    EQ = 7


OPERATORS = {
    PacketType.SUM: lambda x, y: x + y,
    PacketType.MULT: lambda x, y: x * y,
    PacketType.MIN: min,
    PacketType.MAX: max,
    PacketType.GT: lambda x, y: 1 if x > y else 0,
    PacketType.LT: lambda x, y: OPERATORS[PacketType.GT](y, x),
    PacketType.EQ: lambda x, y: 1 if x == y else 0,
}


@dataclass
class Packet:
    version: int
    type_id: int
    length_type_id: Optional[int] = None
    sub: List[Packet] = field(default_factory=list)
    value: Optional[int] = None

    @classmethod
    def decode(
        cls,
        raw: str,
    ) -> Packet:
        b = (c for c in chain(*map(lambda c: f"{int(c,16):04b}", list(raw))))
        return Packet._decode(b)

    @classmethod
    def _decode(
        cls,
        b,
    ) -> Packet:
        packet = Packet(
            version=int("".join([next(b) for _ in range(3)]), 2),
            type_id=int("".join([next(b) for _ in range(3)]), 2),
        )

        if packet.type_id == 4:
            bits = ""
            while True:
                last = next(b) == "0"
                bits += "".join([next(b) for _ in range(4)])
                if last:
                    break
            packet.value = int("".join(bits), 2)
        else:
            packet.length_type_id = int(next(b))
            if packet.length_type_id == 0:
                total_sub_length = int("".join(next(b) for _ in range(15)), 2)
                sb = (next(b) for _ in range(total_sub_length))
                while True:
                    try:
                        packet.sub.append(Packet._decode(sb))
                    except StopIteration:
                        break
            else:
                subpackets_count = int("".join(next(b) for _ in range(11)), 2)
                for _ in range(subpackets_count):
                    packet.sub.append(Packet._decode(b))
        return packet

    def sum_version(self) -> int:
        return reduce(lambda acc, v: acc + v.sum_version(), self.sub, self.version)

    def evaluate(self) -> int:
        if self.value is not None:
            return self.value

        return reduce(
            lambda acc, v: OPERATORS[PacketType(self.type_id)](acc, v),
            map(lambda p: p.evaluate(), self.sub),
        )


def solve_part_one(raw: str) -> int:
    packet = Packet.decode(raw)
    return packet.sum_version()


def solve_part_two(raw: str) -> int:
    packet = Packet.decode(raw)
    return packet.evaluate()


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        raw = input_file.readline().splitlines()[0]

        ret = solve_part_one(raw=deepcopy(raw))
        print(f"part one: {ret}")

        ret = solve_part_two(raw=deepcopy(raw))
        print(f"part two: {ret}")
