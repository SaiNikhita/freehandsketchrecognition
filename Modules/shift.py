import cv2
import numpy as np


def shift_image(img):
    for x in [50, -50]:
        for y in [150, -150]:
            M = np.float32([[1, 0, x], [0, 1, y]])
            (rows, cols) = img.shape[:2]
            result_image = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
            image_name = FILE_NAME.split(".")[0]+"_shift"+str(x) + str(y)+".png"
            cv2.imwrite(image_name, result_image)
            cv2.waitKey(0)
    

FILE_NAME = '482.png'
img = cv2.imread(FILE_NAME)
shiftImage(img)
