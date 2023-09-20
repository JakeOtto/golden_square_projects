#music tracker tests
from lib.music_tracker import*

def test_music_tracker():
    tester = Music_tracker()

    assert tester.return_track_list() == []
    tester.add_track("Dio- Holy Diver")
    tester.add_track("SeaSickSteve- Cut My Wings")
    tester.add_track("BoneyM- Rasputin")

    assert tester.return_track_list() == ["Dio- Holy Diver","SeaSickSteve- Cut My Wings","BoneyM- Rasputin"]


