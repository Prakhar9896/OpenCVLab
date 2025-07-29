import cv2
import numpy as np

img_gray=cv2.imread('../test/pink.jpeg')

for gamma in [0.1,0.5,1.2,2.2]:
    gamma_corrected=np.array(255*(img_gray/255) ** gamma, dtype='uint8')

    cv2.imwrite('gamma_transformed'+str(gamma)+'.jpeg',gamma_corrected)