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

**门限**（只将🌺 主体提取出来）

<img src="ScreenShots/Thresholding/result.png" alt="result" style="zoom:50%;" />

------

## Log变换 | Log Transformations

- **公式：**`s = c * log(1 + r)`
  - `c = 255/log(1 + 255)`时，保持刻度一致
- **用处：**扩展黑像素，压缩白像素（*<u>想观察的信息隐藏在黑色中</u>*）

**原图**

<img src="ScreenShots/Log Transformations/origin.png" alt="origin" style="zoom:50%;" />

**Log变换**

<img src="ScreenShots/Log Transformations/result.png" alt="result" style="zoom:50%;" />

------

## γ变换 | Gamma Transformations

- **公式：**$s = c * r^γ$
- **用处：**色彩校正
  - Gamma变换不仅会改变亮度，而且会改变rgb的比率

### 图像过暗

**原图**

<img src="ScreenShots/Gamma Transformations/toodark.png" alt="toodark" style="zoom:50%;" />

**γ变换**

![result_dark](ScreenShots/Gamma Transformations/result_dark.png)

### 图像过亮

**原图**

<img src="ScreenShots/Gamma Transformations/toobright.png" alt="toobright" style="zoom:50%;" />

**γ变换**

![result_bright](ScreenShots/Gamma Transformations/result_bright.png)

------

## 分段线型函数

### 对比度拉伸 ｜ Contrast Stretching

扩展图像灰度级动态范围，可以跨越记录介质和显示装备的全部灰度范围

#### Logistic函数 | 生长函数

- **函数模型：**
  $$
  \frac{1}{1 + (m/r)^E} , \ m,E为常数
  $$

- **函数图像：**

  <img src="ScreenShots/Contrast Stretching/growth_function_figure.png" alt="image-20191012174901680" style="zoom:50%;" />

- **函数分析：**

  - 原始函数模型的定义域和值域都是[0, 1]

  - **参数：**

    - m：图像x方向的中心点，该点的函数值也为中心

    - E：控制图像上升的速度和分段数**(E越大，上升的速率越快)**

      <img src="ScreenShots/Contrast Stretching/growth_function_E_1.png" alt="image-20191012175902662" style="zoom:50%;" />

      <img src="ScreenShots/Contrast Stretching/growth_function_E_2.png" alt="image-20191012180220900" style="zoom:50%;" />

- **函数变换：**

  - 通过m调节横坐标的范围（m在这里相当于常量）

    > 在图像处理时将m取成255/2，可以使得横坐标从0～255

  - 通过引入常量a调节纵坐标的范围
    $$
    \frac{a}{1 + (a * m/r)^E}
    $$

    > 在图像处理时将a取成255，可以使得纵坐标拉伸到255

    
    
  - 通过引入常量deltax进行x轴平移，用适当的方式调节黑色区域和白色区域的映射
    $$
    \frac{a}{1 + (\frac{a * m}{(r + deltax)^E})}
    $$
    

- **最终的函数模型：**

  ```matlab
  a = 255;
  E = 10;
  r = 0:0.1:255;
  
  s = a ./ (1 + (a*0.5./r).^E);
  ```

  <img src="ScreenShots/Contrast Stretching/growth_model.png" alt="growth_model" style="zoom:50%;" />

------

#### 两点线性 ｜ Piece Wise Linear

- **函数模型：**

  <img src="ScreenShots/Contrast Stretching/PieceWice_model.png" alt="PieceWice_model" style="zoom:50%;" />

**原图**

![origin1](ScreenShots/Contrast Stretching/origin1.png)

**对比度拉伸**

![target1](ScreenShots/Contrast Stretching/target1.png)

**原图**

![origin2](ScreenShots/Contrast Stretching/origin2.png)

**对比度拉伸**

![target2](ScreenShots/Contrast Stretching/target2.png)

------

