import cv2
import numpy as np

img = cv2.imread('sample.png', 0)

vertical_inverted_img = cv2.flip(img, 0)
horizontal_inverted_img = cv2.flip(img, 1)

(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), -25, 1.0)
cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])

nW = int((h * sin) + (w * cos))
nH = int((h * cos) + (w * sin))

M[0, 2] += (nW / 2) - cX
M[1, 2] += (nH / 2) - cY

rotated = cv2.warpAffine(img, M, (nW, nH), borderValue=(255, 255, 255))

cv2.imshow("Rotated", rotated)

cv2.imwrite('rotated.png', rotated)

cv2.waitKey(0)
