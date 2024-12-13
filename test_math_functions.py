import pytest
from math_functions import multiply, divide, distance, solve_quadratic, geometric_sum

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

def test_distance():
    assert distance(0, 0, 3, 4) == 5

def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (2, 1)
    assert solve_quadratic(1, 2, 1) == -1
    assert solve_quadratic(1, 0, 1) == "No real roots"

def test_geometric_sum():
    assert geometric_sum(1, 2, 3) == 7
