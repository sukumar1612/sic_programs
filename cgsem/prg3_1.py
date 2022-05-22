import cv2
import numpy as np
import random   

image = cv2.imread('lenna_grayscale.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)

print(ret)
cv2.imshow("lenna", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()