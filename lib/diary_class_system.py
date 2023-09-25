#diary_class_system
from lib.todo import*
from lib.todo_list import*
from lib.diary_entry import*
import re

class Diary_system:
    def __init__(self):
        self.diary_entry_list = []
        self.todo_list = TodoList()
        self.contact_dict = {}

    def add_diary_entry(self,diary_entry):
        diary_key = diary_entry.entry_title
        self.contact_dict[diary_key](self.find_phone_numbers(diary_contents))
        self.diary_entry_list.append(diary_entry)


    def read_diary_entries(self):
        return self.diary_entry_list()
    

    # def read_on_time(self,time_avalible, wpm):
    #     time_to_read_dict = {}
    #     for entry in self.diary_entry_list:
    #         time_to_read_dict[entry]=entry.reading_time(wpm)
    #     closest_time = min(list(time_to_read_dict.values()), key=lambda x:abs(x-time_avalible))
    #     diary_entry = [key for key, value in time_to_read_dict.items() if value == closest_time][0]
    #     return diary_entry.diary_contents

    # def add_todo_entry(self,todo):
    #     self.todo_list.append(todo)

    # def return_contact_list(self):
    #     return self.contact_list()


    def find_phone_numbers(input_string):
        # Define a regular expression pattern to match 11-digit phone numbers
        pattern = r'\b\d{11}\b'

    #     # Use re.findall to find all matching phone numbers in the input string
        phone_numbers = re.findall(pattern, input_string)

        return phone_numbers




# =========================================================
# use cases - record experiences

#             read recorded experiences

#             select diary by read time - based on time and wpm

#             implement a todo list 

#             implement a contacts list - taken from numbers in diary

# -------------------------------------------
# diary system class 

# - add entry     ------------
#       diary entry class
# - read entries 
# - select entry to read based on time and wpm
# - todo list ---------------
#     todo class - with list of todo's in main class
# - contact list - dictionary - taken fromn numbers in diary

# ==========================================================

# # As a user
# So that I can record my experiences
# I want to keep a regular diary

# As a user
# So that I can reflect on my experiences
# I want to read my past diary entries

# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed

# As a user
# So that I can keep track of my tasks
# I want to keep a todo list along with my diary

# As a user
# So that I can keep track of my contacts
# I want to see a list of all of the mobile phone numbers in all my diary entries