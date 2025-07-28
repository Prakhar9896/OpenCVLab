import cv2

# Read the image
img = cv2.imread("pink.jpeg")

# Resize image: width = 300, height = 300
resized = cv2.resize(img, (300, 300))

# Show result
cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
