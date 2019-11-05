# 空间滤波

[TOC]

------

## 概念

Moving a filter mask over the image and computing the sum of products at each location.

用一个pattern，将中心位置在图像上移动，计算小**临域**内的**加权平均**，得到新像素值

------

## 相关 | Correlation

$$
g(x,y) = \sum_{s=-1}^a\sum_{t=-b}^b h(s,t)f(x+s,y+t)
$$



------

## 卷积 | Convolution

$$
g(x,y) = \sum_{s=-1}^a\sum_{t=-b}^b h(s,t)f(x-s,y-t)
$$

**一维公式：**
$$
g(x) = \sum_{s=-1}^a h(s)f(x-s)
$$

------

## MATLAB方法(还没具体试验)

- fspecial
- imfilter
- conv2
- colfilt
- medfilt2
- ordfilt2