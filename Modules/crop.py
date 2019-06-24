def crop_image(image, height, width):
    img_height, img_width = image.shape[:2]
    top = (img_height - height) // 2
    left = (img_width - width) // 2
    cropped = image[top:img_height-top, left:img_width-left]
    return cropped