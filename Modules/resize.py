import os
import cv2

DATASET_PATH = r'C:\Users\AASHRITH\Desktop\FreeHandSketchProject\zoom'


def resize_image():
    for roots, directories, files in os.walk(DATASET_PATH):
        for file in files:
            path_of_sample = os.path.join(roots, file)
            print(path_of_sample)
            img = cv2.imread(path_of_sample, 0)
            resized = cv2.resize(img, dsize=(224, 224))
            cv2.imwrite(path_of_sample, resized)


resize_image()
