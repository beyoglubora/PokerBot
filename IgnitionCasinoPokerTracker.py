from PokerGame import *
import CardDetector
import ActionDetector
import PlayerDetector
import cv2
import numpy as np


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
        self.scale_image_width = .4
        self.scale_image_height = .4
        self.track_new_game = True  # start tracking for a new game immediately

    def capture(self):
        """
        Takes a screen shot of the game
        """

    def track_poker_game(self):
        """
        Publishes events that occur within the poker game to event queue
        """
        image = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (0, 0), fx=self.scale_image_width, fy=self.scale_image_height)
        if self.track_new_game:
            self.track_new_game = self.should_detect_new_game(image)

    def should_detect_new_game(self, image):
        """
        Determines if tracking for new game is necessary. Will delegate detection work for determining if a new game has
        started to various detectors.
        :return: if a new game has started
        """
        requirements_satisfied = True
        if not self.poker_game.has_players():
            requirements_satisfied = False
            PlayerDetector.detect_players(image, self.poker_game)
        if not self.poker_game.has_button():
            requirements_satisfied = False
            PlayerDetector.detect_button(image, self.poker_game)
        if not self.poker_game.has_small_blind():
            requirements_satisfied = False
            ActionDetector.detect_small_blind(self.poker_game.button)
        if not self.poker_game.has_big_blind():
            requirements_satisfied = False
            ActionDetector.detect_big_blind(self.poker_game.button)
        if not self.poker_game.has_our_num():
            requirements_satisfied = False
            PlayerDetector.detect_our_num(image, self.poker_game.button)
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
