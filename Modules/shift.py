import numpy as np
import os

def shift_image(img, roots, file):
    for x in [50, -50]:
        for y in [150, -150]:
            M = np.float32([[1, 0, x], [0, 1, y]])
            (rows, cols) = img.shape[:2]
            result_image = cv2.warpAffine(img, M, (cols, rows), borderValue=(255, 255, 255))
            image_name = file.split(".")[0] + "_shift " + str(x) + str(y) + ".png"
            cv2.imwrite(os.path.join(roots, image_name), result_image)
