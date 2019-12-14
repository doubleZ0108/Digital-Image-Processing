# 航拍图像、行车记录仪图像道路提取

[TOC]

------

## 运行环境

- **开发软件：**PyCharm 2019.1.3
- **python版本：**3.7.4
- **主要依赖：**cv2, numpy

------

## 如何运行

1. 图片资源在`Resources/`目录下
   - `road.jpg`: 行车记录仪图像
   - `track.png`: 航拍机场图像
2. 项目代码在`src/`目录下
   - `Standard_Hough.py`: 标准霍夫边缘提取机场跑道线
   - `ProgressiveProbability_Hough.py`: 渐进概率式霍夫变换提取机场跑道线
   - `LaneLine_Segmentation.py`: 航拍图像道路提取

------

## 项目结构

```
.
├── README.md
├── Resources
│   ├── road.jpg
│   └── track.png
├── doc
│   └── 航拍图像、行车记录仪图像道路提取.pdf
└── src
    ├── LaneLine_Segmentation.py
    ├── ProgressiveProbability_Hough.py
    └── Standard_Hough.py

3 directories, 7 files
```

------

## 关于作者

| 作者姓名 | 张喆                                     |
| -------- | ---------------------------------------- |
| 学校     | Tongji University                        |
| 联系方式 | doubleZ0108@163.com                      |
| 版权信息 | ©doubleZ tongji Univ. All Right Reserved |

