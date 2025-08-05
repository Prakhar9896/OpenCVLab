import cv2
import numpy as np

image = cv2.imread('./test/pink.jpeg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Image not found or unable to open")

laplacian = cv2.Laplacian(image, cv2.CV_64F)

laplacian_abs = cv2.convertScaleAbs(laplacian)

cv2.imwrite('laplacian_edges.jpg', laplacian_abs)

print("Laplacian edge detection done and saved as laplacian_edges.jpg")
