from typing import List

import pytest

from day_16 import solver
from day_16.solver import Packet


@pytest.mark.parametrize(
    "encoded, decoded",
    [
        (
            "D2FE28",
            Packet(version=6, type_id=4, value=2021),
        ),
        (
            "38006F45291200",
            Packet(
                version=1,
                type_id=6,
                length_type_id=0,
                sub=[
                    Packet(version=6, type_id=4, value=10),
                    Packet(version=2, type_id=4, value=20),
                ],
            ),
        ),
        (
            "EE00D40C823060",
            Packet(
                version=7,
                type_id=3,
                length_type_id=1,
                sub=[
                    Packet(version=2, type_id=4, value=1),
                    Packet(version=4, type_id=4, value=2),
                    Packet(version=1, type_id=4, value=3),
                ],
            ),
        ),
    ],
)
def test_decode(encoded: str, decoded: Packet):
    assert Packet.decode(encoded) == decoded


@pytest.mark.parametrize(
    "encoded, version_sum",
    [
        ("D2FE28", 6),
        ("38006F45291200", 9),
        ("EE00D40C823060", 14),
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ],
)
def test_part_one(encoded: str, version_sum: int):
    assert solver.solve_part_one(encoded) == version_sum


@pytest.mark.parametrize(
    "encoded, value",
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ],
)
def test_part_two(encoded: str, value: int):
    assert solver.solve_part_two(encoded) == value
