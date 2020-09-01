# 天文图像去噪

* [运行环境](#运行环境)
* [如何运行](#如何运行)
* [项目结构](#项目结构)
* [关于作者](#关于作者)

------

## 运行环境

- **开发软件：**PyCharm 2019.1.3
- **python版本：**3.7.4
- **主要依赖：**imageio, skimage, numpy, cv2, pylab

------

## 如何运行

1. 安装相应的依赖

   > 例如安装skimage
   >
   > ```bash
   > pip install skimage
   > ```
   >
   > 但是请注意
   >
   > >  这时候会报错Please install the `scikit-image` package (instead of `skimage`)
   > >
   > > 所以按照提示操作即可：
   > >
   > > pip install scikit-image
   > >
   > > 环境安装成功。
   > >
   > > ![截屏2019-11-1118.23.47.png](https://upload-images.jianshu.io/upload_images/12014150-62acae614cc63ff3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
   > >
   > > ![截屏2019-11-1118.24.04.png](https://upload-images.jianshu.io/upload_images/12014150-160a495d189ab8e3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
   > >
   > > 
   >
   > ⚠️同时请注意同时要安装视频解码工具
   >
   > ```bash
   > pip install imageio-ffmpeg
   > ```
   >
   > ![截屏2019-11-1118.24.48.png](https://upload-images.jianshu.io/upload_images/12014150-7d57099afbd5debd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. 将`Resources`目录下的两个天文图像视频放到相应位置

3. 运行`src/GenerateDenoisedFrame.py`可实验图像平滑操作

4. 运行`src/RunningAverage_with_FrameAlignment.py`可实验图像增强操作

   - 运行时输出的数字为当前处理到的帧位置，可以方便观察

------

## 项目结构

```
.
├── README.md
├── Resources
│   ├── sky_1.avi
│   └── sky_2.avi
├── doc
│   └── 天文图像去噪项目文档.md
└── src
    ├── GenerateDenoisedFrame.py
    ├── RunningAverage_with_FrameAlignment.py
    └── ShowFrame.py

3 directories, 7 files
```

------

## 关于作者

| 作者姓名 | 张喆                                     |
| -------- | ---------------------------------------- |
| 学校     | Tongji University                        |
| 联系方式 | doubleZ0108@163.com                      |
| 版权信息 | ©doubleZ tongji Univ. All Right Reserved |

