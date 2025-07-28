import cv2

image_gray=cv2.imread('../test/pink.jpeg',0)

cv2.imshow('grayscale image',image_gray)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('grayscale.jpeg',image_gray)