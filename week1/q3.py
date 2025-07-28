import cv2

image = cv2.imread("../test/pink.jpeg")

x = 50 
y = 100

(b, g, r) = image[y, x]
print(f"B: {b}, G: {g}, R: {r}")

print(f"RGB: ({r}, {g}, {b})")
