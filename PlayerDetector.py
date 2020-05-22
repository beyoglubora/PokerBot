import numpy as np
import cv2
import IgnitionCasinoConstants as igc
import CardDetector


def detect_players(image, poker_game):
    _, thresh = cv2.threshold(image, igc.PLAYER_TAG_THRESHOLD, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    player_tag_contours = []

    for cnt in contours:
        if igc.PLAYER_TAG_AREA_MIN_BOUND < cv2.contourArea(cnt) < igc.PLAYER_TAG_AREA_MAX_BOUND:
            player_tag_contours.append(cnt.reshape((cnt.shape[0], 2)))

    for cnt in player_tag_contours:
        px1 = int(np.min(cnt, axis=0)[0]) - igc.HALF_PLAYER_BOX_WIDTH
        py1 = int(np.min(cnt, axis=0)[1]) - igc.HALF_PLAYER_BOX_HEIGHT
        px2 = int(np.max(cnt, axis=0)[0]) + igc.HALF_PLAYER_BOX_WIDTH
        py2 = int(np.max(cnt, axis=0)[1]) + igc.HALF_PLAYER_BOX_HEIGHT

        player_box_image = image[px1:px2, py1:py2]

        if CardDetector.has_cards(player_box_image):
           player_number = get_player_number_from_player_box()
           poker_game.set_player_box[player_number] = [px1, py1, px2, py2]



def detect_button(image, poker_game):
    return


def detect_our_num(image, poker_game):
    return
