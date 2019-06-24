import os
import cv2
import numpy as np

from shift import shift_image
from zoom import zoom_image
from mirroring import mirror_image
from rotate import rotate_image

DATASET_PATH = r'C:\Users\Vanitha\Desktop\project\Dataset\png'

def mirror_images():
    for roots, directories, files in os.walk(DATASET_PATH):
        for file in files:
            path_of_sample = os.path.join(roots, file)
            img = cv2.imread(path_of_sample, 0)
            mirrored_image = mirror_image(img)
            image_name = roots + "\\" + file.split(".")[0] + "mirror.png"
            cv2.imwrite(image_name, mirrored_image)

def rotate_images():
    for roots, directories, files in os.walk(DATASET_PATH):
        for file in files:
            path_of_sample = os.path.join(roots, file)
            img = cv2.imread(path_of_sample, 0)
            os.remove(path_of_sample)
            kernel = np.ones((5, 5), np.uint8)
            img_erosion = cv2.erode(img, kernel, iterations=1)
            for angle in [0, 15, 30, 90, -15, -30]:
                rotated_image = rotate_image(img_erosion, angle)
                image_name = roots + "\\" + file.split('.')[0] + "_" + str(angle) + ".png"
                cv2.imwrite(image_name, rotated_image)


def shift_images():
    for roots, directories, files in os.walk(DATASET_PATH):
        for file in files:
            path_of_sample = os.path.join(roots, file)
            img = cv2.imread(path_of_sample, 0)
            shift_image(img, roots, file)


def zoom_images():
    for roots, directories, files in os.walk(DATASET_PATH):
        for file in files:
            path_of_sample = os.path.join(roots, file)
            img = cv2.imread(path_of_sample, 0)
            for percentage in [3, 7, -3, -7]:
                zoomed_image = zoom_image(img, percentage, 0)
                image_name = file.split(".")[0] + "_" + str(percentage) + ".png"
                cv2.imwrite(os.path.join(roots, image_name), zoomed_image)



