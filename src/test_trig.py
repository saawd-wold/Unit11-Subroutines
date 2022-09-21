from maths.trigonometry import PI, sin, cos, tan
from maths.util import NaN
from math import isnan
import pytest
import numpy as np

def test_PInotChanged():
    assert PI == 3.14159265358979

def test_sinZero():
    assert sin(0) == 0.0

def test_sinPi():
    assert sin(PI) == 0.0

def test_sinNPi():
    for n in range(2, 30, 3):
        assert sin(n*PI) == 0.0, f"sin({n}*PI) is incorrect"

def test_sinPIoverTwo():
    assert sin(PI/2) == pytest.approx(1.0, 1e-5)

def test_sinPeriodicity():
    for _ in range(10):
        r = np.random.random() * 2 * PI - PI
        s = sin(r)
        for n in range(1, 11):
            assert sin(r + n * 2 * PI) == s
            assert sin(r - n * 2 * PI) == s

def test_sinPiOver6():
    assert sin(PI/6) == pytest.approx(0.5, 1e-5)
def test_sinPiOver4():
    assert sin(PI/4) == pytest.approx(np.sqrt(2)/2, 1e-5) 
def test_sinPiOver3():
    assert sin(PI/3) == pytest.approx(np.sqrt(3)/2, 1e-5) 

def test_cosZero():
    assert cos(0) == pytest.approx(1.0, 1e-8)

def test_cosPi():
    assert sin(PI) == pytest.approx(-1.0, 1e-8)

def test_sinNPi():
    for n in range(2, 30, 3):
        assert sin(n*PI) == pytest.approx((-1.0)**n, 1e-8), f"cos({n}*PI) is incorrect!"

def test_cosPIoverTwo():
    assert sin(PI/2) == pytest.approx(0.0, 1e-5)

def test_cosPeriodicity():
    for _ in range(10):
        r = np.random.random() * 2 * PI - PI
        c = cos(r)
        for n in range(1, 11):
            assert cos(r + n * 2 * PI) == c
            assert cos(r - n * 2 * PI) == c

def test_cosPiOver6():
    assert cos(PI/6) == pytest.approx(np.sqrt(3)/2, 1e-5)
def test_cosPiOver4():
    assert sin(PI/4) == pytest.approx(np.sqrt(2)/2, 1e-5) 
def test_cosPiOver3():
    assert sin(PI/3) == pytest.approx(1/2, 1e-5) 


def test_tanZero():
    assert tan(0) == pytest.approx(0.0, 1e-8)

def test_tanPi():
    assert sin(PI) == pytest.approx(0.0, 1e-8)

def test_tanNPi():
    for n in range(2, 30, 3):
        assert tan(n*PI) == pytest.approx(0.0, 1e-8), f"tan({n}*PI) is incorrect!"

def test_tanPIoverTwo():
    assert isnan(tan(PI/2)), "Did not get NaN value for tan(PI/2)"

def test_tanPeriodicity():
    for _ in range(10):
        r = np.random.random() * 2 * PI - PI
        c = cos(r)
        if c == 0:
            continue
        t = tan(r)
        for n in range(1, 11):
            assert tan(r + n * 2 * PI) == t
            assert tan(r - n * 2 * PI) == t

def test_tanPiOver6():
    assert tan(PI/6) == pytest.approx(1/np.sqrt(3), 1e-5)
def test_cosPiOver4():
    assert tan(PI/4) == pytest.approx(1, 1e-8) 
def test_cosPiOver3():
    assert tan(PI/3) == pytest.approx(np.sqrt(3), 1e-5) 

