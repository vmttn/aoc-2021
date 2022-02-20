from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Entry:
    patterns: List[str]
    digits: List[str]


def solve_part_one(notes: List[Entry]) -> int:
    return sum(
        len([digit for digit in entry.digits if len(digit) in [2, 4, 3, 7]])
        for entry in notes
    )


NUMBER_BY_SEGMENTS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def solve_part_two(notes: List[Entry]) -> int:
    output_values_sum = 0

    for entry in notes:
        # 1. Find wire/segment mapping
        activation_count_by_wire = dict(Counter("".join(entry.patterns)))

        one_wires = next(pattern for pattern in entry.patterns if len(pattern) == 2)
        four_wires = next(pattern for pattern in entry.patterns if len(pattern) == 4)
        seven_wires = next(pattern for pattern in entry.patterns if len(pattern) == 3)
        eight_wires = next(pattern for pattern in entry.patterns if len(pattern) == 7)

        wire_by_segment = {
            "a": next(w for w in seven_wires if w not in one_wires),
            "f": next(w for w, c in activation_count_by_wire.items() if c == 9),
            "b": next(w for w, c in activation_count_by_wire.items() if c == 6),
            "e": next(w for w, c in activation_count_by_wire.items() if c == 4),
        }
        wire_by_segment["c"] = next(w for w in one_wires if w != wire_by_segment["f"])
        wire_by_segment["d"] = next(
            w for w in four_wires if w not in wire_by_segment.values()
        )
        wire_by_segment["g"] = next(
            w for w in eight_wires if w not in wire_by_segment.values()
        )

        segment_by_wire = {w: s for s, w in wire_by_segment.items()}

        # 2. Decode number
        figures = []
        for digit in entry.digits:
            segments = "".join(sorted([segment_by_wire[w] for w in digit]))
            figures.append(NUMBER_BY_SEGMENTS[segments])

        output_values_sum += int("".join(map(str, figures)))

    return output_values_sum


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        notes = [
            Entry(*list(map(lambda s: s.strip().split(" "), line.split("|"))))
            for line in input_file
        ]

        ret = solve_part_one(notes=notes)
        print(f"part one: {ret}")

        ret = solve_part_two(notes=notes)
        print(f"part two: {ret}")
