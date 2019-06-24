import cv2
import numpy as np


def mirror_image(img):
    mirrored_img = cv2.flip(img, 1)
    cv2.imwrite("mirror_image.png", mirrored_img)


img = cv2.imread('482.png', 0)
mirrorImage(img)