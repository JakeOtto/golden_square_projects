#testing the counter class
from lib.counter import *

def test_counter():
    new_counter = Counter()
    new_counter.add (5)
    result = new_counter.report()
    assert result == "Counted to 5 so far."

    new_counter.add (13)
    result = new_counter.report()
    assert result == "Counted to 18 so far."
