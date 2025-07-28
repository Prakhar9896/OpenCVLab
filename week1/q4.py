import cv2

# Read the image
img = cv2.imread("pink.jpeg")

# Draw rectangle: cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)

# Show result
cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
