# 图像复原

[TOC]

------

## 图像退化-复原模型

- degraded -- restore --> restoration

- **退化:** degradation function + aditive noise
  $$
  g(x,y) = h(x,y) \bigotimes f(x,y) + \eta(x,y)
  $$

------

## Mean Filter | 均值滤波器

### Arithmetic Mean | 算数均值

- compute the average of corrupted image in the area defined by a neighborhood window
- **blur** the image to remove noise

$$
\hat{f}(x,y) = \frac{1}{MN}\sum_{(s,t)\in S_{x,y}}g(s,t)
$$

------

### Geometic Mean | 几何均值

- 与算数均值的平滑效果相当
- 但可以丢失更少的图像细节

$$
\hat{f}(x,y) = [\prod_{(s,t)\in S_{x,y}}g(s,t)]^{\frac{1}{MN}}
$$

------

### Harmonic | 谐波均值

- 可以处理salt noise，但是不能处理pepper noise

  > 像素等于0时分母太大了，产生无效值，原像素完全不占主导地位

- **可以当作公平性的损失函数**

$$
\hat{f}(x,y) = \frac{MN}{\sum \limits_{(s,t)\in S_{x,y}} \frac{1}{g(s,t)}}
$$

------

### Conharmonic | 逆谐波均值

- 可以处理salt & pepper noise，但不能同时处理二者

- Q>0，消除pepper noise

  Q<0，消除salt noise

$$
\hat{f}(x,y) = \frac{\sum \limits_{(s,t)\in S_{x,y}}g(s,t)^{Q+1}}{\sum \limits_{(s,t)\in S_{x,y}}g(s,t)^{Q}}
$$

------

## Order Statistic Filter | 统计排序

ordering{ranking} the value of the pixels contained in the image area encompassed by the filter

### Mean | 中值

- less blurring the linear something filter
- **单极或双级脉冲下效果尤其好**

$$
\hat{f}(x,y) = \mathop{median}_{(s,t)\in S_{x,y}}\{g(s,t)\}
$$

------

### Max/Min | 最大值/最小值

- max filter --> pepper noise (取最大值，把黑色的干掉)

  min filter --> salt noise

$$
\hat{f}(x,y) = \max_{(s,t)\in S_{x,y}}\{g(s,t)\}
$$

$$
\hat{f}(x,y) = \min_{(s,t)\in S_{x,y}}\{g(s,t)\}
$$

------

### Midpoint | 中点

- 计算最大值和最小值的均值
- good for Gaussian, uniform

$$
\hat{f}(x,y) = \frac{1}{2}[\max_{(s,t)\in S_{x,y}}\{g(s,t)\} \ + \min_{(s,t)\in S_{x,y}}\{g(s,t)\}]
$$

------

### Alpha-Trimmed Mean | 修正的alpha均值

- 用于解决salt & pepper太多了，median还是噪声
- 可以应对多种噪声叠加 (比如salt & pepper + Gaussian)
- 删掉$\frac{d}{2}$lowest，$\frac{d}{2}$highest，剩下$MN-d$个像素为$g_r$

$$
\hat{f}(x,y) = \frac{1}{MN-d}\sum \limits_{(s,t)\in S_{xy}}g_r(s,t)
$$



