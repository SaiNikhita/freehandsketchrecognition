import cv2
import numpy as np

FILE_NAME = '482.png'

for x in [50, -50]:
    for y in [150, -150]:
        M = np.float32([[1, 0, x], [0, 1, y]])
        try:
            img = cv2.imread(FILE_NAME)
            (rows, cols) = img.shape[:2]
            res = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
            name = FILE_NAME.split(".")[0]+"_shift"+str(x) + str(y)+".png"
            cv2.imwrite(name, res)
            cv2.waitKey(0)
        except IOError:
            print('Error while reading files !!!')
