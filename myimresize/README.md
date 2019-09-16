# 「imresize」Realization

[TOC]

------

## Description

In this project, you can resize your image which is `SCALE` times the size of the origin one, and the image you input can be a `grayscale`, `RGB` and the height & width of the image can be `1 to 1` or `n to 1`(n is a real number).

------

## Development Environment

- **Development Environment: **macOS Mojave 10.14.6
- **Development Software: **MATLAB_R2019a
- **Development Language: **matlab

------

## How To Run

1. You should put the fellowing matlab script in your working path.
   - `myimresize.m`
   - `Nearest.m`
   - `Bilinear.m`
   - `Bicubic.m`
2. You can write your own program in this working path.
3. In your own program, firstly, you should use `imread()` to load your image.
4. Then, you can use `myimresize(img, scale, algorithm)` to resize your image.
   - parameter `img`: the matrix you just load by `imread()`
   - parameter `scale`: the scale you want to resize for the image
   - parameter `algorithm`: you can choose which algorithm will be used in the program
     - `nearest`: Nearest Neighbor Interpolation Algorithm
     - `bilinear`: Bilinear Interpolation Algorithm
     - `bicubic`: Bicubic Interpolation Algorithm
   - result value: the new image with the SCALE`times the size of the origin one
5. You can use `imshow(new_img, []);`to observe the result.

------

## Experiment



------

## Realization



------

## About the Author

| Item            | Info                     |
| --------------- | ------------------------ |
| **Name**        | Zhe Zhang(张喆)          |
| **ID**          | 1754060                  |
| **Adviser**     | Prof. Qingjiang Shi      |
| **Course Name** | Digital Image Processing |
| **Course Time** | Tue. 2-4 [1-17]          |
| **Email**       | doubleZ0108@163.com      |

------

## Project Structure

```
.
├── Bicubic.m
├── Bilinear.m
├── Nearest.m
├── README.md
├── Resources
│   ├── color1.jpg
│   ├── color2.jpg
│   ├── gray1.jpg
│   └── gray2.jpg
├── myimresize.m
└── test.m
```

------

