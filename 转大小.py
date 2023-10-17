import cv2 as cv
img = cv.imread('train_image/train035.png')
img = cv.resize(img, dsize=(1920, 1080))
cv.imwrite('train_image/train035.jpg',img)