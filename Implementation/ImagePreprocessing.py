import os
import cv2
import numpy as np

DATASET_PATH = r'C:\Users\Anudeep\Desktop\Projects\Free Hand Sketch Recognition\Dataset\png\png'

for roots, directories, files in os.walk(DATASET_PATH):
    for file in files:
        path_of_sample = os.path.join(roots, file)
        print(path_of_sample)
        img = cv2.imread(path_of_sample, 0)
        os.remove(path_of_sample)
        kernel = np.ones((5, 5), np.uint8)
        img_erosion = cv2.erode(img, kernel, iterations=1)
        for angle in range(0, 360, 5):
            (h, w) = img_erosion.shape[:2]
            (cX, cY) = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))
            M[0, 2] += (nW / 2) - cX
            M[1, 2] += (nH / 2) - cY
            rotated = cv2.warpAffine(img_erosion, M, (nW, nH), borderValue=(255, 255, 255))
            dim = (1111, 1111)
            resized = cv2.resize(rotated, dim)
            name = file.split('.')[0] + "_" + str(angle) + ".png"
            cv2.imwrite(os.path.join(roots, name), resized)