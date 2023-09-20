#test file for diary snippet
from lib.diary_exercise import *

def test_make_snippet():
    result = make_snippet("On this day, today, of all day was my day, the day where i got into the office before derrick, so i got the donuts i wanted, ohh that sweet jelly glaze")
    assert result == "On this day, today, of ..."

def test_est_time_to_read():
    result = est_time_to_read("here's a string of six words")
    assert result == "Hmm to read this, it would probably take your slow ass 0.03 minutes"