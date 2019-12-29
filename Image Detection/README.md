# 图像检测

[TOC]

------

- 一阶导：较粗的边缘
- 二阶导：精细细节（细线，孤立点，噪声）
  - 二阶导会产生双边缘效应
  - 二阶导的符号：边缘的过渡是从亮到暗还是从暗到亮

------

## 孤立点检测

**Laplacian operator**
$$
\nabla^{2} f=\frac{\partial^{2} f}{\partial x^{2}}+\frac{\partial^{2} f}{\partial y^{2}}
$$

$$
g(x, y)=\left\{\begin{array}{l}{1, \text { if }|R(x, y)| \geq T} \\ {0, \text { otherwise }}\end{array}\right.
$$

- T是threshold

  > 影响threshold的因素
  >
  > - noise 噪声
  > - illumination 光照
  > - reflectance 反射

