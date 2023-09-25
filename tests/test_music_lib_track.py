#testing_music_lib_track
from lib.music_library import*
from lib.track import*

# intergration tests ======================================
# -add feature calling track
def test_intergrated_add():
    test_track = Track ("Rip & Tear","Mike Gordon")
    test_library = MusicLibrary()
    test_library.add(test_track)
    assert test_library.library_dict == {"Rip & Tear":"Mike Gordon"}

# -search after add, after calling track
def test_intergrated_search():
    test_track = Track ("Rip & Tear","Mike Gordon")
    test_track01 = Track ("Wish you were here","Pink Floyd")
    test_track02 = Track ("Money","Pink Floyd")
    test_library = MusicLibrary()
    test_library.add(test_track)
    test_library.add(test_track01)
    test_library.add(test_track02)
    result = test_library.search("Pink Floyd")
    assert result == ["Wish you were here:Pink Floyd", "Money:Pink Floyd"]

# unit tests ======================================
# -library add feature without trackx inheritance
# def test_mock_add():
#     test_library = MusicLibrary()
#     mock_track = {"War":"Low Rider"}
#     mock_track.title = "Low Rider"
#     mock_track.artist = "War"
#     test_library.add(mock_track)
#     assert test_library.library_dict == {"War":"Low Rider"}

# # -search feature without Track
# def test_mock_search():
#     test_library = MusicLibrary()
#     mock_track = {"Mastodon":"Toes to toes"}
#     mock_track.title = "Toes to toes"
#     mock_track.artist = "Mastodon"
#     test_library.add(mock_track)
#     result = test_library.search("Mastodon")
#     assert result == [{"Mastodon":"Toes to toes"}]


# -track matches works 
def test_track_match():
    test_track = Track("4:00A.M.","Taeko Onuki")
    assert test_track.matches("Taeko Onuki") == True



#============

# class MusicLibrary:
#     # Public properties:
#     #   tracks: a list of instances of Track

#     def __init__(self):
#         pass

#     def add(self, track):
#         # track is an instance of Track
#         # Track gets added to the library
#         # Returns nothing
#         pass

#     def search(self, keyword):
#         # keyword is a string
#         # Returns a list of instances of track that match the keyword
#         pass



# class Track:
#     def __init__(self, title, artist):
#         # title and artist are both strings
#         pass

#     def matches(self, keyword):
#         # keyword is a string
#         # Returns true if the keyword matches either the title or artist
#         pass