import cv2


def crop_image(image, height, width):
    img_height, img_width = image.shape[:2]
    top = (img_height - height) // 2
    left = (img_width - width) // 2
    cropped = img[top:img_height-top, left:img_width-left]
    return cropped


img = cv2.imread("zoom.png", 0)
crop_img = crop_image(img, 1111, 1111)
cv2.imwrite("cropped.png", crop_img)