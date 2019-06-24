import cv2
import numpy as np

img = cv2.imread('482.png', 0)
cv2.imshow("original", img)

horizontal_inverted_img = cv2.flip(img, 1)
cv2.imshow("mirrored", horizontal_inverted_img)
cv2.imwrite("result.png", horizontal_inverted_img)

cv2.waitKey(0)