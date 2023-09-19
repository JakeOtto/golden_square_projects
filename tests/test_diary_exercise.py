#test file for diary snippet
from lib.diary_exercise import *

def test_make_snippet():
    result = make_snippet("On this day, today, of all day was my day, the day where i got into the office before derrick, so i got the donuts i wanted, ohh that sweet jelly glaze")
    assert result == "On this day, today, of ..."