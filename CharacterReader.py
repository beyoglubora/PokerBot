import cv2
import IgnitionCasinoConstants as igc

stack_reference_chars = cv2.imread("Game/IgnitionCasinoStackCharacters.png", cv2.IMREAD_GRAYSCALE)
_, stack_reference_chars = cv2.threshold(stack_reference_chars, igc.STACK_CHARS_THRESHOLD, 255, cv2.THRESH_BINARY_INV)
stack_reference_contours, _ = cv2.findContours(stack_reference_chars, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
stack_reference_contours = sorted(stack_reference_contours, key=lambda ctr: cv2.boundingRect(ctr)[0])


def read_stack_chars(image):
    _, image = cv2.threshold(image, igc.STACK_CHARS_THRESHOLD, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

    chars = ""
    for ctr in contours:
        comparisons = list(map(lambda ref_ctr: cv2.matchShapes(ctr,ref_ctr,1,0), stack_reference_contours))
        i = comparisons.index(min(comparisons))
        if i == 10:
            chars += "$"
        elif i == 11:
            chars += "."
        else:
            chars += str(i)
    return chars


print(read_stack_chars(cv2.imread("Game/Stack_209.png",cv2.IMREAD_GRAYSCALE)))