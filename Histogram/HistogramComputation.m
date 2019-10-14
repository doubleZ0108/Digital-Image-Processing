clc;
clear;

I = imread('Resources/gray1.jpg');
[M,N] = size(I);

%% 库函数
imhist(I);

%% 循环逐像素统计
% h = zeros(1, 255);
% for xa=1:M
%     for xb=1:N
%         pixel = I(xa, xb);
%         h(pixel) = h(pixel) + 1;
%     end
% end
% plot(h);
