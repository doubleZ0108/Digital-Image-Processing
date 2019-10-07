# 灰度变换函数 | Basic Intensity Transformation Functions

[TOC]

------

## 图像反转 | Image Negatives

- **灰度级范围：**`[0, L-1]`

- **公式：**`s = L - 1 - r`

- **库函数：**

  ```matlab
  negatives_I = imcomplement(I);
  ```

- **用处：**增强嵌入图像暗色区域的白色或灰色细节，特别是当黑色面积在尺寸上占主导地位时。

**原图**

<img src="ScreenShots/Negatives/origin.png" alt="origin" style="zoom: 50%;" />

**反转**

<img src="ScreenShots/Negatives/result.png" alt="result" style="zoom:50%;" />

------

## 门限 | Thresholding

- **公式：**
  $$
  s = \left\{\begin{array}{1}{1, r > threshold} \\ 0, otherwise\end{array}\right.
  $$

- **库函数：**

  ```matlab
  % 定义门限值，注意范围是0～1
  threshold = 0.5;
  J = im2bw(I, threadhold);
  ```

- **用处：**将感兴趣的物体从背景中孤立出来 -> 分割

**原图**

<img src="ScreenShots/Thresholding/origin.jpg" alt="origin" style="zoom:50%;" />

**门限**（只将花主体提取出来）

<img src="ScreenShots/Thresholding/result.png" alt="result" style="zoom:50%;" />

------

