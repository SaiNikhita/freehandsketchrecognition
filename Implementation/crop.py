import cv2
img = cv2.imread("zoom.png")
crop_img = img[83:1194, 0:1111]
cv2.imshow("cropped", crop_img)
cv2.imwrite("cropped.png", crop_img)
cv2.waitKey(0)