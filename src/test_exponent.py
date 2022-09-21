import pytest
from maths.exponents import exp, exponentiate, sqrt, root, EULER
from maths.util import NaN
from math import isnan
import numpy as np

def test_EulerUnchanged():
    assert EULER == 2.718281828459, "You changed the value of Euler's Constant!!!"

def test_exp0():
    assert exp(0) == 1

def test_expN():
    for n in range(-10, 0):
        assert exp(n) == pytest.approx(1/(EULER**n), 1e-7)
    for n in range(0, 10):
        assert exp(n) == pytest.approx((EULER**n), 1e-7)

def test_expFloat():
    p = 1.5
    assert exp(p) == pytest.approx((EULER ** 3) / (EULER ** 2), 1e-4)
    p = 1/8 + 1/16
    assert exp(p) == pytest.approx((EULER ** 3) / (EULER ** 16), 1e-4)

def test_expNaN():
    assert isnan(exp(NaN))

def test_expo1():
    for a in np.random.choice(np.linspace(0, 100, 10000), 50, replace=False):
        assert exponentiate(a, 1) == a, f"{a}^1 did not yield {a}!"

def test_expobase1():
    for a in np.random.choice(np.linspace(0, 100, 10000), 50, replace=False):
        assert exponentiate(1, a) == 1, f"1^{a} did not yield {1}!"

def test_expo_arbitrarynumbers():
    A = np.random.gamma(1.618, 28.024, 50) + 1e-4
    B = np.random.normal(0, 15, 50)
    pows = np.float_power(a, b)
    for a, b, p in zip(A, B, pows):
        assert exponentiate(a, b) == pytest.approx(p, 1e-5)

def test_expo0():
    for a in np.random.choice(np.linspace(0, 100, 10000), 50, replace=False):
        assert exponentiate(a, 0) == 1, f"{a}^0 did not yield 1!"

def test_sqrt_AOK():
    N = [1, 4, 25, 36, 49, 81, 169, 196, 625]
    R = [1, 2, 5, 6, 7, 9, 13, 14, 25]

    for n, r in zip(N, R):
        assert sqrt(n) == pytest.approx(r, 1e-8)

def test_sqrt_neg():
    assert isnan(sqrt(-1))

def test_root_n():
    bases = np.arange(2, 12)
    powers = np.arange(2, 12)
    vs = np.power(bases, powers)
    for b, p, v in zip(bases, powers, vs):
        assert root(v, p) == pytest.approx(b, 1e-8)

def test_root_n_negative_success():
    bases = np.arange(-2, -12, -1)
    powers = np.arange(2, 12) * 2 + 1
    vs = np.power(bases, powers)
    for b, p, v in zip(bases, powers, vs):
        assert root(v, p) == pytest.approx(b, 1e-8)

def test_root_n_negative_failure(capsys):
    result = root(-3, 1.23)
    assert capsys.out == "Use exponentiate to compute non-integer roots, n must be integer type!"
