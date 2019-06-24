import cv2
img = cv2.imread('sample.png', 0)
height, width = img.shape[:2]
newHeight, newWidth = height + 15/100 * height, width
zoom = cv2.resize(img, (int(newHeight), int(newWidth)))
print(zoom.shape[:2])
cv2.imshow("Original Image", img)
cv2.imshow("Zoomed image", zoom)
cv2.imwrite("zoom.png", zoom)
cv2.waitKey(0)