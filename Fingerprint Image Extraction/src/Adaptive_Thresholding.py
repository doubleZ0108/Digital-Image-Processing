'''
@program: Adaptive_Thresholding.py

@description: 自适应阈值处理

@author: doubleZ

@create: 2019/12/14 
'''
import cv2

def Adaptive_Thresholding(image):
    '''
    :description: 自适应阈值处理

    :param image: 原图

    :return gray: 原图的灰度图像
    :return thresh: 简单阈值处理后的图像
    :return th1_1: adaptive Mean thresholding 阈值处理后的图像
    :return th2: adaptive Gaussian thresholding 阈值处理后的图像
    '''
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)     # rgb图像变换为灰度图像

    blurred = cv2.medianBlur(gray, 1)       # 高斯滤波降噪

    (T, thresh) = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)   # 简单阈值处理

    th1 = cv2.adaptiveThreshold(gray, 255,
                                cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)   # 自适应阈值处理

    th1_1 = cv2.medianBlur(th1, 5)      # adaptive mean thresholding

    th2 = cv2.adaptiveThreshold(gray, 255,
                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)   # adaptive gaussian thresholding

    return [gray, thresh, th1_1, th2]


if __name__ == "__main__":
    image = cv2.imread('../Resources/article.png')

    [gray, thresh, th1_1, th2] = Adaptive_Thresholding(image)

    cv2.imshow('Original Image', gray)
    cv2.imshow('Global Thresholding (v = 127)', thresh)
    cv2.imshow('Adaptive Mean Thresholding', th1_1)
    cv2.imshow('Adaptive Gaussian Thresholding', th2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()