'''
@program: Otsu_Thresholding.py

@description: Otsu最佳全局阈值处理

@author: doubleZ

@create: 2019/12/14 
'''
import cv2

def Otsu_Thresholding(image):
    '''
    :description: Otsu最佳全局阈值

    :param image: 原图

    :return gray: 原图的灰度图像
    :return thresh: 简单阈值处理后的图像
    :return th1: 对灰度图像进行Otsu最佳全局阈值处理后对图像
    :return blurred: 高斯模糊后的图像
    :return th2:对高斯滤波后的图像进行Otsu最佳全局阈值处理后的图像
    '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)     # rgb图像变换为灰度图像

    (T, thresh) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 简单阈值处理

    (T, th1) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # 对灰度图像进行Otsu最佳全局阈值处理

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)     # 高斯滤波降噪

    (T, th2) = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # 对高斯滤波后对图像进行Otsu最佳全局阈值处理

    return [gray, thresh, th1, blurred, th2]

if __name__ == "__main__":

    image = cv2.imread('../Resources/bubble.jpeg')

    [gray, thresh, th1, blurred, th2] = Otsu_Thresholding(image)

    cv2.imshow('Original Noisy Image', gray)
    cv2.imshow('Global Thresholding (v=127)', thresh)
    cv2.imshow("Otsu's Thresholding", th1)
    cv2.imshow('Gaussian filtered Image', blurred)
    cv2.imshow("Otsu's Thresholding", th2)


    cv2.waitKey(0)
    cv2.destroyAllWindows()