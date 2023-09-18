#test_codeword_checker
from lib.check_codeword import *

def test_check_codeword():
    
    input_string = str


    result_horse = check_codeword("horse")
    assert result_horse == "Correct! Come in."

    result_cat = check_codeword("cat")
    assert result_cat == "WRONG!"
    
    result_home = check_codeword("home")
    assert result_home == "Close, but nope."


    # result_close = check_codeword(input_string)


# def check_codeword(codeword):
#     if codeword == "horse":
#         return "Correct! Come in."
#     elif codeword[0] == "h" and codeword[-1] == "e":
#         return "Close, but nope."
#     else:
#         return "WRONG!"