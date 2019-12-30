# 图像分割

Segmentation based on thresholding

[TOC]

------

## Basic global thresholding

### 聚类分割

找到两个像素集合，让他们的距离[用一个像素代表一个结合]比较远（分得比较开）

1. 选一个全局阈值的初值T（通常是图像的average grey level）

2. 用T分割图像，得到两组像素

   - G1: 灰度值小于T的所有像素集合
   - G2: 灰度值大于T的所有像素集合

3. 计算G1，G2的平均灰度m1，m2

4. 更新阈值
   $$
   T = \frac{m_1 + m_2}{2}
   $$

5. 循环2～4，直到连续两次迭代的T值之差小于pre-defined的$\Delta T$（连续两次的门限差别不大）

------

## Otsu's optimum global thresholding





------

## Variable thresholding



