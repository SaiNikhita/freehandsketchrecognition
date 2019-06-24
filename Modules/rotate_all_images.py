import os
import cv2
import numpy as np

from rotate import rotate_image


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


rotate_images()