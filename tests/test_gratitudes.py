#tests for gratitudes
from lib.gratitudes import *

def test_gratitudes():

    new_gratitude = Gratitudes()

    new_gratitude.add("pizza")
    new_gratitude.format()

    result = new_gratitude.format()
    assert result == "Be grateful for: pizza"

