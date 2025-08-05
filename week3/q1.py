import cv2
import numpy as np

image = cv2.imread('./test/galaxy.webp', cv2.IMREAD_COLOR)
if image is None:
    raise ValueError("Image not found or unable to open")

image_float = np.float32(image)

blurred = cv2.GaussianBlur(image_float, (9, 9), 10.0)

unsharp_image = cv2.addWeighted(image_float, 1.5, blurred, -0.5, 0)

unsharp_image = np.clip(unsharp_image, 0, 255).astype(np.uint8)

cv2.imwrite('unsharp_masked.jpg', unsharp_image)

print("Unsharp masking applied and saved as unsharp_masked.jpg")
