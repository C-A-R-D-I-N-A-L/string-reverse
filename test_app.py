import pytest
from app import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh", "Test failed for input 'hello'"
    assert reverse_string("Python") == "nohtyP", "Test failed for input 'Python'"
    assert reverse_string("") == "", "Test failed for empty input"
    assert reverse_string("a") == "a", "Test failed for single character"
    assert reverse_string("12345") == "54321", "Test failed for numeric string"