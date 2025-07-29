import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../test/pink.jpeg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found or unable to open.")
    exit()

equalized_img = cv2.equalizeHist(img)
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Histogram Equalized Image')
plt.imshow(equalized_img, cmap='gray')
plt.axis('off')

plt.show()
