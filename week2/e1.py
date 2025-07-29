import cv2
import numpy as np

img_gray=cv2.imread('../test/pink.jpeg',0)

cv2.imshow('gray scale image',img_gray)
cv2.waitKey(0)

c=255/(np.log(1+np.max(img_gray)))

log_transformed=c*np.log(1+img_gray)

log_transformed=np.array(log_transformed,dtype=np.uint8)

cv2.imwrite('log_transformed_img.jpeg',log_transformed)