import os
import cv2
import numpy as np
from shift import shift_image


DATASET_PATH = r'C:\Users\Vanitha\Desktop\project\Dataset\png'

def shift_images():
    for roots, directories, files in os.walk(DATASET_PATH):
        for file in files:
            path_of_sample = os.path.join(roots, file)
            img = cv2.imread(path_of_sample, 0)
            shift_image(img, roots, file)