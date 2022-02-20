from __future__ import annotations
from pathlib import Path
from typing import List, Tuple


def solve_part_one(diagnostic_report: List[int], word_length: int) -> Tuple[int, int]:
    one_count_by_index = [0] * word_length

    for value in diagnostic_report:
        for index in range(word_length):
            one_count_by_index[index] += (value >> (word_length - 1 - index)) & 1

    gamma_rate = int(
        "".join(
            [
                str(1) if count >= len(diagnostic_report) - count else str(0)
                for count in one_count_by_index
            ]
        ),
        2,
    )
    epsilon_rate = ~gamma_rate & (2 ** word_length - 1)
    return gamma_rate, epsilon_rate


def solve_part_two(diagnostic_report: List[int], word_length: int) -> Tuple[int, int]:
    oxygen_generator_rating = co2_scrubber_rating = -1

    selected_values = list(diagnostic_report)
    for index in range(word_length):
        gamma_rate, _ = solve_part_one(
            selected_values,
            word_length=word_length,
        )

        selected_values = [
            value
            for value in selected_values
            if (gamma_rate ^ value) >> (word_length - index - 1) & 1 == 0
        ]

        if len(selected_values) == 1:
            oxygen_generator_rating = selected_values.pop()
            break

    selected_values = list(diagnostic_report)
    for index in range(word_length):
        _, espilon_rate = solve_part_one(
            selected_values,
            word_length=word_length,
        )

        selected_values = [
            value
            for value in selected_values
            if (espilon_rate ^ value) >> (word_length - index - 1) & 1 == 0
        ]

        if len(selected_values) == 1:
            co2_scrubber_rating = selected_values.pop()
            break

    return oxygen_generator_rating, co2_scrubber_rating


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        diagnostic_report = [int(line, 2) for line in input_file]

        gamma_rate, espilon_rate = solve_part_one(diagnostic_report, word_length=12)
        print(f"part one: {gamma_rate * espilon_rate}")

        oxygen_generator_rating, co2_scrubber_rating = solve_part_two(
            diagnostic_report, word_length=12
        )
        print(f"part two: {oxygen_generator_rating * co2_scrubber_rating}")
