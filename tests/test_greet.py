#test for greet
from lib.greet import *

def test_greet():
    name = str
    result = greet(name)
    assert result == str(f"Hello, {name}!")