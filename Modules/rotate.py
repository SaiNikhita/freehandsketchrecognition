import cv2
import numpy as np


def rotate_image(img, angle):
    (height, width) = img.shape[:2]
    (centerX, centerY) = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D((centerX, centerY), angle, 1.0)
    cos = np.abs(rotation_matrix[0, 0])
    sin = np.abs(rotation_matrix[0, 1])
    new_width = int((height * sin) + (width * cos))
    new_height = int((height * cos) + (width * sin))
    rotation_matrix[0, 2] += (new_width / 2) - centerX
    rotation_matrix[1, 2] += (new_height / 2) - centerY
    rotated = cv2.warpAffine(img, rotation_matrix, (new_width, new_height), borderValue=(255, 255, 255))
    dim = (1111 , 1111)
    resized = cv2.resize(rotated, dim)
    return resized
