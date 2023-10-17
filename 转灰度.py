import cv2
import numpy as np
import torchvision.transforms as transforms


def cv2_BGR2Gray():
    # ======================== 读取图片 =======================
    # 图片路径，相对路径
    image_path = "D:\计算机视觉\PWG cut\juchizhuang.jpg"
    # 读取图片,格式为BGR
    image = cv2.imread(image_path)

    # ======================== 显示图片 =======================
    # 缩放图片
    width = int(image.shape[0] / 2)
    height = int(image.shape[1] / 2)
    image = cv2.resize(image, (height, width), interpolation=cv2.INTER_CUBIC)
    # 显示图片
    cv2.imshow('girl_bgr', image)

    # ============== 转为灰度图，并显示灰度图片 ================
    # 转为灰度图像
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 显示图片
    cv2.imshow('girl_gray', image)
    cv2.waitKey(0)


if __name__ == '__main__':
    cv2_BGR2Gray()