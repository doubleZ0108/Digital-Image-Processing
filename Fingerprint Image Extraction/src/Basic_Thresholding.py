'''
@program: Basic_Thresholding.py

@description: 简单阈值处理

@author: doubleZ

@create: 2019/12/14 
'''
import cv2

def Basic_Thresholding(img):
    '''
    :description: 简单阈值处理

    :param img: 灰度图像

    :return : 阈值处理后的图像
    '''
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    (T, thresh_inv) = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)
    return thresh_inv


if __name__ == "__main__":
    image = cv2.imread('../Resources/snow.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)     # rgb图像变换为灰度图像

    thresh_inv = Basic_Thresholding(gray)   # 阈值处理后的图像

    image_mask = cv2.bitwise_and(gray, gray, mask=thresh_inv)   # 在阈值处理后的图像上加掩膜

    cv2.imshow('original image', image)
    cv2.imwrite('../Resources/original.png', image)
    cv2.imshow('thresh_inv', thresh_inv)
    cv2.imwrite('../Resources/thresh_inv.png', thresh_inv)
    cv2.imshow('image_mask', image_mask)
    cv2.imwrite('../Resources/image_mask.png', image_mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()