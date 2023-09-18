#testing_report_length
from lib.report_length import *

def test_report_length():
    result = report_length("Here's a string")
    assert result == "This string was 15 characters long."

def test_report_length_2():
    result = report_length("small str")
    assert result == "This string was 9 characters long."

def test_report_length_3():
    result = report_length("big old string in here")
    assert result == "This string was 22 characters long."


