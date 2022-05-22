import cv2
import numpy as np
import random   

image = cv2.imread('lenna_grayscale.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(0, len(image)):
    for j in range(0, len(image[0])):
        image[i][j] = 255-image[i][j]

cv2.imshow("lenna", image)
cv2.waitKey(0)
cv2.destroyAllWindows()