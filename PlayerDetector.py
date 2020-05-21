import numpy as np
import cv2


def detect_players(image, poker_game):
    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
    cv2.imshow("image", img)
    cv2.waitKey()
    return


def detect_button(image, poker_game):
    return


def detect_our_num(image, poker_game):
    return
