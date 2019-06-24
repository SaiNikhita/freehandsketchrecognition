import cv2
from crop import crop_image

def zoom_image(image, percentage_height, percentage_width):
    height, width = image.shape[:2]
    newHeight = int(height + percentage_height/100 * height)
    newWidth = int(width + percentage_width/100 * width)
    zoomed = cv2.resize(img, dsize=(newHeight, newWidth))
    return crop_image(zoomed, height, width)