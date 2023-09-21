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

    def add_diary_entry(self,diary_entry,diary_contents):
        diary_entry = DiaryEntry(diary_entry,diary_contents)
        self.contact_dict[diary_entry](self.find_phone_numbers(diary_contents))
        self.diary_entry_list.append(diary_entry)


    # def read_diary_entries(self):
    #     return self.diary_entry_list()
    
    # def read_on_time(self,time_avalible, wpm):
    #     time_to_read_dict = {}
    #     for entry in self.diary_entry_list:
    #         time_to_read_dict[entry]=entry.reading_time(wpm)
    #     closest_time = min(list(time_to_read_dict.values()), key=lambda x:abs(x-time_avalible))
    #     diary_entry = [key for key, value in time_to_read_dict.items() if value == closest_time][0]
    #     return diary_entry.diary_contents

    # def add_todo_entry(self,todo_name,todo_discription):
    #     todo_name = Todo(todo_discription)
    #     self.todo_list.list_of_tasks.append(todo_name)

    # def return_contact_list(self):
    #     return self.contact_list()


    # def find_phone_numbers(input_string):
    #     # Define a regular expression pattern to match 11-digit phone numbers
    #     pattern = r'\b\d{11}\b'

    #     # Use re.findall to find all matching phone numbers in the input string
    #     phone_numbers = re.findall(pattern, input_string)

    #     return phone_numbers


test_diary_system = Diary_system()
test_diary_system.add_diary_entry("Monday11th","well it was rubbish day but met this cute girl who kept asking me about things i liked to eat at mcdonalds, maybe becuase she works there, told me to reach her on 07434298476, careful she has a mad, one eyed dog")
test_diary_system.add_diary_entry("Tuesday 12th","man she did work there, the number was for customer feedback")
# test_diary_system.add_diary_entry("23/4/23","nobody i know died in south central la, today was a good day, just ring up father Dolally on 07722078463")
# test_diary_system.read_diary_entries()
# test_diary_system.add_todo_entry("Cut_grass","oi up, we need to cut old man jenkin's grass, careful he has a mad, one eyed dog")
# test_diary_system.add_todo_entry("Wash up","mann that chick with the fro next door is having a bbq thursday, make sure you wash your face")
# test_diary_system.return_contact_list()





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