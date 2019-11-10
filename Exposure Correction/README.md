# 数字图像处理 --- 欠曝光度图像曝光度校正

[TOC]

------

## 运行环境

- **开发软件：**PyCharm 2019.1.3
- **python版本：**3.7.4
- **主要依赖：**matplotlib, numpy, cv2, 

------

## 如何运行

### Gamma变换

- `src/GammaTransform/`目录下为Gamma变换有关源代码
- `Resources/GammaTransform`目录下为Gamma变换所用到的原始图片

目录下的`.py`文件内含`__main__`，因此可以直接运行；也可以自己编写`.py`文件而把这些文件当作库进行引用

其中`GammaTransform.py`为Gamma变换的核心文件；三个`Processxx.py`文件是应用该核心文件进行的一些小实验

### 直方图均衡化

- `src/Histogram/`目录下为直方图均衡化有关源代码
- `Resources/Histogram目录下为直方图均衡化所用到的原始图片

`GenerateHistogram.py`为生成图像直方图的核心文件；`Histeq.py`为直方图均衡化的核心文件；两个`Processxx.py`文件是应用该核心文件进行的一些小实验

------

## 项目结构



------

## 关于作者

| 作者姓名 | 张喆                                     |
| -------- | ---------------------------------------- |
| 学校     | Tongji University                        |
| 联系方式 | doubleZ0108@163.com                      |
| 版权信息 | ©doubleZ tongji Univ. All Right Reserved |

