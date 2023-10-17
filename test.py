import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('7.png',0)
cv2.imshow('image',img)
cv2.waitKey(0)

plt.imshow(img,'gray')
plt.show()