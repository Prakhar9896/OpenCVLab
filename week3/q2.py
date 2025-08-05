import cv2
import numpy as np

image = cv2.imread('./test/pink.jpeg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Image not found or unable to open")

grad_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

gradient_magnitude = cv2.magnitude(grad_x, grad_y)

gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX)
gradient_magnitude = np.uint8(gradient_magnitude)

cv2.imwrite('gradient_magnitude.jpg', gradient_magnitude)

print("Gradient magnitude saved as gradient_magnitude.jpg")
