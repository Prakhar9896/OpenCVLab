import cv2

image = cv2.imread('./test/galaxy.webp', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Image not found or unable to open")

edges = cv2.Canny(image, 50, 150)

cv2.imwrite('canny_edges.jpg', edges)

print("Canny edge detection done and saved as canny_edges.jpg")
