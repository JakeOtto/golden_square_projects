#tesing for presents
import pytest
from lib.present import *


def test_present():
    new_test_present = Present()
    new_test_present.wrap("something")

    with pytest.raises(Exception) as e: # <-- New code
        new_test_present.wrap("sdgfs")
    error_message = str(e.value) # <-- New code
    assert error_message == "A contents has already been wrapped."


def test_nothing_to_wrap():

    new_test_present = Present()
    
    with pytest.raises(Exception) as e: # <-- New code
        new_test_present.unwrap()
    error_message = str(e.value) # <-- New code
    assert error_message == "No contents have been wrapped."



# class Present:
#     def __init__(self):
#         self.contents = None

#     def wrap(self, contents):
#         if self.contents is not None:
#             raise Exception("A contents has already been wrapped.")
#         self.contents = contents

#     def unwrap(self):
#         if self.contents is None:
#             raise Exception("No contents have been wrapped.")
#         return self.contents