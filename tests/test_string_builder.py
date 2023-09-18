#testing string builder

from lib.string_builder import *

def test_String_Builder():
    new_string_builder = StringBuilder()

    new_string_builder.add("here's a lovely string")
    result = new_string_builder.output()
    assert result == "here's a lovely string"

    result = new_string_builder.size()
    assert result == 22

    

