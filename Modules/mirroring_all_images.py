import os
import cv2
import numpy as np
from mirroring import mirror_image


DATASET_PATH = r'C:\Users\Vanitha\Desktop\project\Dataset\png'

def mirror_images():
    for roots, directories, files in os.walk(DATASET_PATH):
        for file in files:
            path_of_sample = os.path.join(roots, file)
            img = cv2.imread(path_of_sample, 0)
            mirrored_image = mirror_image(img)
            image_name = roots + "\\" + file.split(".")[0] + "mirror.png"
            cv2.imwrite(image_name, mirrored_image)