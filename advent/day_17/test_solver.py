from day_17 import solver


def test_part_one():
    assert solver.solve_part_one(target_area=((20, 30), (-10, -5))) == 45


def test_part_two():
    assert solver.solve_part_two(target_area=((20, 30), (-10, -5))) == 112
