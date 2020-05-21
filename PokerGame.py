class PokerGame:
    def __init__(self):
        self.players = None
        self.player_boxes = {}
        self.sb = None
        self.bb = None
        self.button = None
        self.our_num = None
        self.chips = None
        self.hand = None
        self.stage = None  # pre-flop

    def set_players(self, players):
        self.players = players

    def set_player_box(self, player, player_box):
        self.player_boxes[player] = player_box

    def set_small_blind(self, sb):
        self.sb = sb

    def set_big_blind(self, bb):
        self.bb = bb

    def set_our_num(self, our_num):
        self.our_num = our_num

    def set_chips(self, chips):
        self.chips = chips

    def set_hand(self, hand):
        self.hand = hand

    def set_stage(self, stage):
        self.stage = stage

    def set_button(self, button):
        self.button = button

    def has_players(self):
        return self.players is not None

    def has_small_blind(self):
        return self.sb is not None

    def has_big_blind(self):
        return self.bb is not None

    def has_button(self):
        return self.button is not None

    def has_our_num(self):
        return self.our_num is not None

    def has_chips(self):
        return self.chips is not None

    def has_hand(self):
        return self.hand is not None

    def new_round(self):
        self.players = None
        self.hand = None
        self.stage = 0
