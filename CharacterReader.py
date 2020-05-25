import cv2
import IgnitionCasinoConstants as igc


def get_grayscale_image(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def get_sorted_contours(image, threshold):
    _, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
    return contours


def get_match_indices(image, reference_image, threshold):
    contours = get_sorted_contours(image, threshold)
    reference_contours = get_sorted_contours(reference_image, threshold)
    match_indices = []
    for ctr in contours:
        comparisons = list(map(lambda ref_ctr: cv2.matchShapes(ctr, ref_ctr, 1, 0), reference_contours))
        i = comparisons.index(min(comparisons))
        match_indices.append(i)
    return match_indices


def characters_to_string(image, reference_image, threshold, character_fn):
    match_indices = get_match_indices(image, reference_image, threshold)
    chars = ""
    for i in match_indices:
        chars += character_fn(i)
    return chars


def read_stack_chars(image):
    reference_image = get_grayscale_image("Game/IgnitionCasinoStackReferenceCharacters.png")
    def character_fn(i):
        if i == 10: return "$"
        elif i == 11: return "."
        elif i == 12: return ","
        return str(i)
    return characters_to_string(image, reference_image, igc.STACK_CHARS_THRESHOLD, character_fn)


def read_card_chars(image):
    reference_image = get_grayscale_image("Game/IgnitionCasinoCardReferenceCharacters.png")
    def character_fn(i):
        if i == 10: return "J"
        elif i == 11: return "Q"
        elif i == 12: return "K"
        elif i == 13: return "A"
        elif i == 14: return "c"
        elif i == 15: return "d"
        elif i == 16: return "h"
        elif i == 17: return "s"
        return str(i)
    return characters_to_string(image, reference_image, igc.CARD_CHARS_THRESHOLD, character_fn)


print(read_card_chars(cv2.imread("Game/CardTestImages/4c.png", cv2.IMREAD_GRAYSCALE)))