clear
clc

img = imread('Resources/color2.jpg');
figure;
imshow(img, []);

small_img = myimresize(img, 0.5, 'bicubic');
figure;
imshow(small_img,[]);      % 第二个参数 -> 自动调整数据的范围以便于显示；如果不加第二个参数则矩阵是正确的，但是图像是全白的

big_img = myimresize(img, 2, 'bicubic');
figure;
imshow(big_img, []);