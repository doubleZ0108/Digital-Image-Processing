# 指纹图像提取

* [运行环境](#运行环境)
* [如何运行](#如何运行)
* [项目结构](#项目结构)
* [关于作者](#关于作者)

------

## 运行环境

- **开发软件：**PyCharm 2019.1.3
- **python版本：**3.7.4
- **主要依赖：**cv2, numpy

------

## 如何运行

1. 图片资源在`Resources/`目录下
   - `figurepring.jgp`: `Global_Thresholding.py`处理的图像
   - `snow.png`: `Basic_Thresholding.py`处理的图像
   - `article.png`: `Adaptive_Thresholding.py`处理的图像
   - `bubble.png`: `Otsu_Thresholding.py`处理的图像
2. 项目代码在`src/`目录下
   - `Basic_Thresholding.py`: 简单阈值处理
   - `Adaptive_Thresholding.py`: 自适应阈值处理
   - `Global_Thresholding.py`: 基本全局阈值处理
   - `Otsu_Thresholding.py`: Otsu最佳全局阈值处理

------

## 项目结构

```
.
├── README.md
├── Resources
│   ├── article.png
│   ├── bubble.jpeg
│   ├── fingerprint.jpg
│   └── snow.png
├── doc
│   └── 图像阈值处理项目文档.pdf
└── src
    ├── Adaptive_Thresholding.py
    ├── Basic_Thresholding.py
    ├── Global_Thresholding.py
    └── Otsu_Thresholding.py

3 directories, 10 files
```

------

## 关于作者

| 作者姓名 | 张喆                                     |
| -------- | ---------------------------------------- |
| 学校     | Tongji University                        |
| 联系方式 | doubleZ0108@163.com                      |
| 版权信息 | ©doubleZ tongji Univ. All Right Reserved |

