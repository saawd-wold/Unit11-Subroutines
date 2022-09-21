import pytest
from maths.logarithms import ln, log, EULER
from maths.util import NaN
from math import isnan
import numpy as np

def test_lnE():
    assert ln(EULER) == 1

def test_lnE2():
    assert ln(EULER ** 2) == 2

def test_lognonpositive():
    assert isnan(ln(0))
    assert isnan(log(-1, 7))

def test_log2():
    assert log(256, 2) == pytest.approx(8, 1.e4)