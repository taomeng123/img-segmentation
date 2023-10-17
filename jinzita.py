import cv2
img=cv2.imread("test_data/test_data011_b.jpg")
cv2.imwrite("test_data/test_data011_b.jpg",cv2.pyrUp(img))