from collections import Counter
from functools import reduce
from itertools import chain, tee
from pathlib import Path
from typing import Dict, List, Tuple


def pairwise(iterable):
    """Backport pairwise to python 3.8"""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class Polymer:
    def __init__(self, template: str, rules: List[Tuple[str, str]]):
        self.template = template
        self.pairs = dict(Counter(list(map("".join, pairwise(template)))))
        self.pair_derivatives = dict(
            map(
                lambda k: (
                    k,
                    list(map("".join, pairwise(k[0] + dict(rules)[k] + k[1]))),
                ),
                dict(rules).keys(),
            )
        )

    def grow(self):
        self.pairs = dict(
            reduce(
                lambda acc, v: acc + Counter(dict([v])),
                chain(
                    *map(
                        lambda k: list(
                            chain(
                                map(
                                    lambda derivative: (derivative, self.pairs[k]),
                                    self.pair_derivatives.get(k, []),
                                )
                            )
                        ),
                        self.pairs.keys(),
                    )
                ),
                Counter(),
            )
        )

    def element_counts(self) -> List[Tuple[str, int]]:
        return list(
            map(
                lambda v: (v[0], v[1] // 2),
                (
                    reduce(
                        lambda acc, v: acc + Counter(dict([v])),
                        chain(
                            *map(
                                lambda k: list(
                                    map(lambda c: (c, self.pairs[k]), list(k))
                                ),
                                self.pairs.keys(),
                            )
                        ),
                        Counter(),
                    )
                    + Counter(self.template[0] + self.template[-1])
                ).most_common(),
            )
        )

    def __str__(self) -> str:
        return str(self.element_counts())

    def __len__(self) -> int:
        return len(list(chain(*Counter(self.pairs).elements()))) // 2 + 1


def solve_part_one(
    polymer_template: str, insertion_rules: List[Tuple[str, str]]
) -> int:
    polymer = Polymer(template=polymer_template, rules=insertion_rules)
    for _ in range(10):
        polymer.grow()

    element_counts = polymer.element_counts()

    return element_counts[0][1] - element_counts[-1][1]


def solve_part_two(
    polymer_template: str, insertion_rules: List[Tuple[str, str]]
) -> int:
    polymer = Polymer(template=polymer_template, rules=insertion_rules)
    for _ in range(40):
        polymer.grow()

    element_counts = polymer.element_counts()

    return element_counts[0][1] - element_counts[-1][1]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input"
    with input_path.open("r") as input_file:
        polymer_template = input_file.readline().strip("\n")

        input_file.readline()

        insertion_rules = [tuple(line.strip("\n").split(" -> ")) for line in input_file]

        ret = solve_part_one(
            polymer_template=polymer_template,
            insertion_rules=insertion_rules,
        )
        print(f"part one: {ret}")

        ret = solve_part_two(
            polymer_template=polymer_template,
            insertion_rules=insertion_rules,
        )
        print(f"part two: {ret}")
