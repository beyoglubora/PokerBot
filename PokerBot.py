from IgnitionCasinoPokerTracker import *

pt = IgnitionCasinoPokerTracker("Game")


while True:
    pt.capture()
    pt.track_new_game()
    pt.update_game()
