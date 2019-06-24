import cv2
import numpy as np


def mirror_image(img):
    return cv2.flip(img, 1)


img = cv2.imread('482.png', 0)
mirror_image(img)