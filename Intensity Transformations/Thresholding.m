clear
clc

I = imread('ScreenShots/Thresholding/origin.jpg');

% 定义门限值，注意范围是0～1
threshold = 0.5;

%% im2bw 库函数
J = im2bw(I, threshold);

%% 自定义下限阈值
range = getrangefromclass(I)   % 返回矩阵的范围，这里返回[0, 255]
K = (I>range(2)*threshold);
