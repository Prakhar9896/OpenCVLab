import cv2
import numpy as np

image = cv2.imread('./test/galaxy.webp', cv2.IMREAD_COLOR)
if image is None:
    raise ValueError("Image not found or unable to open")

box_filtered = cv2.blur(image, (5, 5))

gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imwrite('box_filtered.jpg', box_filtered)
cv2.imwrite('gaussian_filtered.jpg', gaussian_filtered)

print("Box filtered image saved as box_filtered.jpg")
print("Gaussian filtered image saved as gaussian_filtered.jpg")
