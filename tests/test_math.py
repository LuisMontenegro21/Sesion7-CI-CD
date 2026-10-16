import importlib.util
from pathlib import Path

import pytest

# math.py tiene el mismo nombre que el módulo estándar de Python, así que un
# "import math" cargaría el de Python. Por eso se carga el archivo por ruta.
_MATH_PATH = Path(__file__).resolve().parent.parent / "math.py"
_spec = importlib.util.spec_from_file_location("mathlib", _MATH_PATH)
mathlib = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mathlib)


# ---------- square ----------

@pytest.mark.parametrize(
    "n, expected",
    [
        (3, 9),
        (-4, 16),
        (0, 0),
        (2.5, 6.25),
    ],
)
def test_square_happy_path(n, expected):
    assert mathlib.square(n) == expected


@pytest.mark.parametrize("n", ["3", None, [3]])
def test_square_invalid_type_raises(n):
    with pytest.raises(TypeError):
        mathlib.square(n)


# ---------- factorial ----------

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
    ],
)
def test_factorial_happy_path(n, expected):
    assert mathlib.factorial(n) == expected


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        mathlib.factorial(-1)


@pytest.mark.parametrize("n", [3.5, "5", True])
def test_factorial_invalid_type_raises(n):
    with pytest.raises(TypeError):
        mathlib.factorial(n)


# ---------- is_prime ----------

@pytest.mark.parametrize("n", [2, 3, 13, 97])
def test_is_prime_true(n):
    assert mathlib.is_prime(n) is True


@pytest.mark.parametrize("n", [-7, 0, 1, 4, 9, 25, 100])
def test_is_prime_false(n):
    assert mathlib.is_prime(n) is False


@pytest.mark.parametrize("n", [7.0, "7", None])
def test_is_prime_invalid_type_raises(n):
    with pytest.raises(TypeError):
        mathlib.is_prime(n)


# ---------- gcd ----------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (12, 18, 6),
        (17, 5, 1),
        (-12, 18, 6),
        (0, 5, 5),
    ],
)
def test_gcd_happy_path(a, b, expected):
    assert mathlib.gcd(a, b) == expected


@pytest.mark.parametrize("a, b", [(1.5, 3), (4, "2"), (True, 2)])
def test_gcd_invalid_type_raises(a, b):
    with pytest.raises(TypeError):
        mathlib.gcd(a, b)


# ---------- lcm ----------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 6, 12),
        (3, 5, 15),
        (-4, 6, 12),
        (0, 5, 0),
    ],
)
def test_lcm_happy_path(a, b, expected):
    assert mathlib.lcm(a, b) == expected


@pytest.mark.parametrize("a, b", [(4.0, 6), ("4", 6), (4, None)])
def test_lcm_invalid_type_raises(a, b):
    with pytest.raises(TypeError):
        mathlib.lcm(a, b)
