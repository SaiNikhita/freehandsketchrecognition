import cv2
import numpy as np


def mirror_image(img):
    return cv2.flip(img, 1)

