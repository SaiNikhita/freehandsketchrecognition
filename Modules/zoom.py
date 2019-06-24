import cv2

def zoom_image(image, percentage_height, percentage_width):
    height, width = image.shape[:2]
    newHeight = int(height + percentage_height/100 * height)
    newWidth = int(width + percentage_width/100 * width)
    zoomed = cv2.resize(img, dsize=(newHeight, newWidth))
    return zoomed


img = cv2.imread('sample.png', 0)
zoomed_image = zoom_image(img, 50, 0)
cv2.imwrite("zoom.png", zoomed_image)