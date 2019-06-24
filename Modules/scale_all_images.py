import cv2
import os
from zoom import zoom_image


DATASET_PATH = r'C:\Users\Anudeep\Desktop\Projects\Free Hand Sketch Recognition\Dataset\temporary'


def zoom_images():
    for roots, directories, files in os.walk(DATASET_PATH):
        for file in files:
            path_of_sample = os.path.join(roots, file)
            img = cv2.imread(path_of_sample, 0)
            for percentage in [3, 7, -3, -7]:
                zoomed_image = zoom_image(img, percentage, 0)
                image_name = file.split(".")[0] + "_" + str(percentage) + ".png"
                cv2.imwrite(os.path.join(roots, image_name), zoomed_image