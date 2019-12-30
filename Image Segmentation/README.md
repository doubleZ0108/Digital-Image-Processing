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

maximize the between-class-variance
$$
\sigma_{B}^{2}=P_{1}(k)\left[m_{1}(k)-m_{G}\right]^{2}+P_{2}(k)\left[m_{2}(k)-m_{G}\right]^{2} \\ \\
\text{optimum threshold} \ \ \ k^{*}=\underset{0 \leq k \leq L-1}{\arg \max } \sigma_{B}^{2}(k)
$$

- $n_i$: 灰度值为i的像素数量
- $p_i = \frac{n_i}{MN}$: 灰度值i出现的概率
- $C_1$: 小于门限的像素集合；$C_2$: 大于门限的像素集合
- $p_1(k) = \sum_{i=0}^{k}p_i$: $C_1$类的均值； $p_2(k) = 1 - p_1(k)$
- $m_G = \sum_{i=0}^{L-1}ip_i$: 全局均值 

1. 计算归一化的直方图，记录$p_i$
2. 计算global mean $m_G$
3. for each 0<=k<=L-1，计算$\sigma_B^2$
4. 找到使$\sigma_B^2$最大化的$k^*$
5. 用$k^*$作为门限分割图像

```matlab
graythresh()			% Otsu's threshold
```

------

## Variable thresholding



