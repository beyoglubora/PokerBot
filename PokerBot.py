import cv2
import CardDetector

img = cv2.imread("PokerTable.png")
crop_img = img[700:1000, 600:1800]
print(CardDetector.detect_cards(crop_img))
