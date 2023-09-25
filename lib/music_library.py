#music_librar_class
# File: lib/music_library.py
from lib.track import*

class MusicLibrary:
    # Public properties:
    #   tracks: a list of instances of Track

    def __init__(self):
        self.library_dict = {}

    def add(self, track):
        self.library_dict[track.title]=track.artist

    def search(self, keyword):
        search_list = []
        for artist,title in self.library_dict.items():
            if keyword in artist or keyword in title:
                search_list.append(f"{artist}:{title}")
        return search_list
    


