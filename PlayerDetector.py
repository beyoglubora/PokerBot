import numpy as np
import cv2
import IgnitionCasinoConstants as igc
import CardDetector
import CharacterReader


def detect_players(image, poker_game):
    """
    This method identifies the coordinates of active players in the Ignition Casino Poker Table.
    :param image: the image of the entire table
    :param poker_game: the internally tracked poker game
    """
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
        player_box_image = image[py1:py2, px1:px2]

        # this check is necessary for players that are seated in the middle of a round
        # (they won't have cards but will have a highlighted player tag that gets contoured)
        if CardDetector.has_cards(player_box_image):
            x, y, w, h = cv2.boundingRect(cnt)
            player_tag_image = image[y:y+h, x:x+w]
            player_number = get_player_number_from_player_box(player_tag_image)
            poker_game.set_player_box(player_number, [px1, py1, px2, py2])


def extract_player_number_from_player_box(player_tag_image):
    """
    :param player_tag_image: image of the bounding box for a single player
    :return: an image of the players assigned number
    """
    _, thresh = cv2.threshold(player_tag_image, igc.PLAYER_TAG_NUMBER_THRESHOLD, 255, cv2.THRESH_BINARY)
    cv2.imshow("image", thresh)
    cv2.waitKey(0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[0]
    x, y, w, h = cv2.boundingRect(contour)
    number_image = thresh[y:y+h, x:x+w]
    return number_image


def get_player_number_from_player_box(player_tag_image):
    """
    :param player_tag_image: image of a players tag including their player number
    :return: the players assigned number in the game
    """
    number_image = extract_player_number_from_player_box(player_tag_image)
    return CharacterReader.read_stack_chars(number_image)


def detect_button(image, poker_game):
    return


def detect_our_num(image, poker_game):
    return
