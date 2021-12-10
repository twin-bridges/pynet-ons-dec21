import sys
import pytest


def func1(x, y):
    return x + y


def func2(x, y):
    return x * y


def test_sum():
    assert func1(10, 99) == 109


def test_product():
    assert func2(7, 9) == 63


@pytest.mark.parametrize(
    "num1, num2, result", [(77, 0, 0), (13, 13, 169), (-1, -1, 1), (-7, 7, -49)]
)
def test_product_params(num1, num2, result):
    assert func2(num1, num2) == result


@pytest.mark.skipif(
    sys.version_info.major == 3 and sys.version_info.minor == 7, reason="because"
)
def test_sum2():
    assert func1(10, 99) == 109
