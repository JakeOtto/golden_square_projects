#diary snippet and more


def make_snippet(input_string):
    string_list = input_string.split(' ')
    
    first_5 = string_list[0:5]
    return_string = ""
    for i in first_5: 
        return_string += (f"{i} ")

    if len(input_string) > 5:
        return (f"{return_string}"+"...")
    else:
        return (return_string)

def est_time_to_read(input_string):
    string_list = input_string.split(' ')
    word_count = len(string_list)
    time = (1/200)*word_count
    
    return (f"Hmm to read this, it would probably take your slow ass {time} minutes")

def verify_punc(input_string):
    accepted_punc = ["!",".","?",":",";"]
    if input_string[0].isupper() and input_string[-1] in accepted_punc:
        return True
    else:
        return False


def check_todo(input_string):
    string_list = input_string.split(' ')
    if "#TODO" in string_list or "#TODO." in string_list:
        return True
    else:
        return False
    

    
def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1

    i = -1
    letter = sorted(counter.items(), key=lambda item: item[1])[i][0]
    if letter == " ":
        i -=1
        letter = letter = sorted(counter.items(), key=lambda item: item[1])[(i)][0]

    return letter






# 1.  describe the problem
# 2.  design the function signature
# 3.  create example tests
# 4.  implement the behaviour

# problem - Make make_snippet - which returns the first 5 words of a string followed by ...
# signature - make_snippet , 1 input string , 1 return string 
# tests - "some really long string here that just keeps going on" == "some really long string here ..."
# # implement - string to list of words, take only first 5 words, remake string with ... 

# problem - estimate time reading
# signature - est_time_to_read  , 1 input string, 1 time signature string output
# tests - "some real string commin in now, a string so long that it would take an ammount of time to read"  == some short time in minutes
# implement - split input to list of words, take length of list, (200 words a minute) 200/length = x x*1 = time in minutes

# problem - verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
# signature - verify_punc, 1 input string, 1 boolean
# tests - "Heres one." = True   "and another" = False 
# implement - check string [0] is upper and check [-1] is a punctuation symbol, return t/f

# problem - check if a text includes the string #TODO.
# signature - check_todo, 1 input string , boolean t/f
# tests - "Heres one #TODO." = True   "and another" = False 
# implement - convert string into list of words , check for #TODO in list, return t/f

