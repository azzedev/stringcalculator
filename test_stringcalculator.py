import pytest
import random
from stringcalculator import stringcalculator

@pytest.mark.parametrize("a, b, expected", [
    (1, 0, 1),
    (1, 1, 2),
])
def test_stringcalculator(a, b, expected):
    assert stringcalculator(a, b) == expected


def test_stringcalculator_random():
    for _ in range(10):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        expected = a + b
        assert stringcalculator(a,b) == expected

def test_stringcalculator_3param():
    assert stringcalculator(1,0,0) == 1