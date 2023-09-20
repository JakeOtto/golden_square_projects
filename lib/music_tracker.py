#music tracker

class Music_tracker:

    def __init__(self):
        self.track_list = []
        

    def add_track(self, track_details):
        self.track_list.append(track_details)

    def return_track_list(self):
        return self.track_list


# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.


# 1.  describe the problem
# 2.  design the function signature
# 3.  create example tests
# 4.  implement the behaviour


# problem - want to be able to create and edit a list of tracks
# signature - musictracker - inputs - songs names, returns - list
# tests - add feature , see all tacks,
# behaviour - create instance of class - create assosiated list of tracks
#             populate class with add method - add to track list
#             return list of all tracks when called