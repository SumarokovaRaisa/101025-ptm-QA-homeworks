import pytest
from simple_math import SimpleMath

simple_math = SimpleMath()


def test_square():
    res = simple_math.square(2)
    assert res == 4


def test_cube():
    res = simple_math.cube(-3)
    assert res == -27

def test_square_negative():
    res = simple_math.square(-3)
    assert res == 9

def test_cube_with_zero():
    res = simple_math.cube(0)
    assert res == 0