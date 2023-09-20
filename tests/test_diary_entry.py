#test file
from lib.diary_entry import*


def test_diary_entry():
    test_entry = DiaryEntry("Test entry","here would be a long string to test stuff")

    
    assert test_entry.format() == "Test entry:here would be a long string to test stuff"

    assert test_entry.count_words() == 9

    assert test_entry.reading_time(50) == ((1/50)*9)

    assert test_entry.reading_chunk(50,1) == "here would be a long string to test stuff"