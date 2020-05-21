from PokerGame import *
import CardDetector
import BetDetector
import PlayerDetector


class IgnitionCasinoPokerTracker:
    """
    A poker game tracker for ignition casino that keeps track of a poker game internally
    """
    def __init__(self, path):
        """
        :param path: Specified path where screenshots of the game are stored
        """
        self.path = path
        self.poker_game = PokerGame()
        self.track_new_game = True  # start tracking for a new game immediately

    def capture(self):
        """
        Takes a screen shot of the game
        """

    def track_poker_game(self):
        """
        Publishes events that occur within the poker game to event queue
        """
        if self.track_new_game:
            self.track_new_game = self.should_detect_new_game()

    def should_detect_new_game(self):
        """
        Determines if tracking for new game is necessary. Will delegate detection work for determining if a new game has
        started to various detectors.
        :return: if a new game has started
        """
        requirements_satisfied = True
        if not self.poker_game.has_players():
            requirements_satisfied = False
            PlayerDetector.detect_players()
        if not self.poker_game.has_button():
            requirements_satisfied = False
            PlayerDetector.detect_button()
        if not self.poker_game.has_small_blind():
            requirements_satisfied = False
            BetDetector.detect_small_blind(self.poker_game.get_button())
        if not self.poker_game.has_big_blind():
            requirements_satisfied = False
            BetDetector.detect_big_blind(self.poker_game.get_button())
        if not self.poker_game.has_our_num():
            requirements_satisfied = False
            self.detect_our_num()
        if not self.poker_game.has_hand():
            requirements_satisfied = False
            CardDetector.detect_hand()
        if requirements_satisfied:
            return False
        else:
            return True

    def update_game(self, events):
        """
        :param events: list of events that will be used to update the game
        :return: none
        """
