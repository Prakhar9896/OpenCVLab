import cv2

# Read the image
img = cv2.imread("pink.jpeg")

# Get image dimensions
(h, w) = img.shape[:2]

# Compute the rotation matrix (rotate 90 degrees around center)
center = (w // 2, h // 2)
matrix = cv2.getRotationMatrix2D(center, 90, 1.0)  # 90-degree rotation

# Apply rotation
rotated = cv2.warpAffine(img, matrix, (w, h))

# Show result
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
