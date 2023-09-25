    #diary exercise, to test
class DiaryEntry:
    def __init__(self, title, contents):
        self.entry_title = title
        self.entry_contents = contents
        self.checkpoint = 0
        #   title: string
        #   contents: string
        

    def format(self):
        return (f"{self.entry_title}:{self.entry_contents}")
        
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        

    def count_words(self):
        string_list = self.entry_contents.split()
        return len(string_list)
        # Returns:
        #   int: the number of words in the diary entry
        

    def reading_time(self, wpm):
        words = self.count_words()
        time_min =  words/wpm 
        return time_min

        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.


    def reading_chunk(self, wpm, minutes):

        string_list = self.entry_contents.split()

        how_many_words = wpm*minutes

        if self.checkpoint == 0:
        
            if how_many_words <= len(string_list):
                checkpoint = how_many_words
                return self.entry_contents[0:how_many_words]
            
            elif how_many_words > len(string_list):
                return self.entry_contents

        elif self.checkpoint > 0:

            if how_many_words <= (len(string_list) - self.checkpoint):
                return self.entry_contents[checkpoint:(checkpoint+how_many_words)]
            
            elif how_many_words > (len(string_list) - self.checkpoint):
                remainder = ((checkpoint + how_many_words)-len(string_list))
                to_return = self.entry_contents[checkpoint:(checkpoint+how_many_words)]+" "+[self.entry_contents[0:remainder]]
                checkpoint = remainder
                return to_return


        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        
