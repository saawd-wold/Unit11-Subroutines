from maths.util import factorial
import pytest
from math import isnan

def test_factorial0():
    assert factorial(0) == 1, "Factorial of 0 is incorrect!"

def test_factorial5():
    assert factorial(5) == 120, "Factorial of 5 is incorrect!"

def test_factorialnegative():
    assert isnan(factorial(-1))