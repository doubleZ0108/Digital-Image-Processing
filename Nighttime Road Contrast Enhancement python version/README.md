# 监控照片对比度增强

* [运行环境](#运行环境)
* [如何运行](#如何运行)
* [项目结构](#项目结构)
* [关于作者](#关于作者)

------

## 运行环境

- **开发软件：**PyCharm 2019.1.3
- **python版本：**3.7.4
- **主要依赖：**matplotlib.peplot, matplotlib.image, cv2, dumpy

------

## 如何运行

1. 安装相应的依赖

   > 例如安装matplotlib
   >
   > ```bash
   > pip install matplotlib
   > ```

2. 将`Resources`目录下的三个夜间行车记录仪图像放到相应位置

3. 运行`src/NightRoad_GammaTransform.py`可实验Gamma变换在夜间行车记录仪图像上的处理

   - `src/GammaTransform.py`为Gamma变换的核心算法

4. 运行`src/NightRoad_Histeq.py`可实验普通直方图均衡化在夜间行车记录仪图像上的处理

   - `src/Histeq.py`为普通直方图均衡化的核心算法

5. 运行`src/NightRoad_Adapthisteq.py`可实验自适应直方图均衡化在夜间行车记录仪图像上的处理

   - `src/AdaptHisteq.py`为自适应直方图均衡化的核心算法

------

## 项目结构

```
.
├── README.md
├── Resources
│   ├── dark_road_1.jpg
│   ├── dark_road_2.jpg
│   └── dark_road_3.jpg
├── doc
│   └── 监控照片对比度增强.pdf
└── src
    ├── AdaptHisteq.py
    ├── GammaTransform.py
    ├── Histeq.py
    ├── NightRoad_Adapthisteq.py
    ├── NightRoad_GammaTransform.py
    └── NightRoad_Histeq.py

3 directories, 11 files
```

------

## 关于作者

| 作者姓名 | 张喆                                     |
| -------- | ---------------------------------------- |
| 学校     | Tongji University                        |
| 联系方式 | doubleZ0108@163.com                      |
| 版权信息 | ©doubleZ tongji Univ. All Right Reserved |

