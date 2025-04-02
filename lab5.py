import pytest
from math_operations import add, multiply

@pytest.fixture
def sample_numbers():
  return (3, 5)

def test_add(sample_numbers):
  a, b = sample_numbers
  assert add(a, b) == 8

def test_multiply(sample_numbers):
  a, b = sample_numbers
  assert multiply(a, b) == 15
  
@pytest.mark.parametrize("a, b, expected", [
  (1, 2, 3),
  (3, 3, 6),
  (-1, 1, 0),
  (0, 0, 0)
])
def test_add_param(a, b, expected):
  assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
  (2, 3, 6),
  (0, 5, 0),
  (-2, 3, -6)
])
def test_multiply_param(a, b, expected):
  assert multiply(a, b) == expected
