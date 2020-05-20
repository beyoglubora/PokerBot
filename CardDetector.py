import numpy as np
import cv2

_image_height = 960
_image_width = 540
_min_contour_area = 10000


def detect_cards(img):
    """
    This function detects all the cards in an image. Assumes the cards are fully visible with no overlap.
    * Currently Work-in-progress. Right now it returns number of cards instead of a list of card images.
    :param img: input image
    :return: list of detected card images
    """
    img = cv2.resize(img, (_image_height, _image_width))
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imggray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    card_contours = []
    for cnt in contours:
        if cv2.contourArea(cnt) > _min_contour_area:
            card_contours.append(cnt)
    return len(card_contours)
