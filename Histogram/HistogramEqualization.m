clc;
clear;

I = imread('Resources/origin2.png');
I = rgb2gray(I);
[M,N] = size(I);

s = zeros(1, 256);
[counts, pixels] = imhist(I);   % [每个像素的个数 | 像素值(0～255)]

sum_count = 0;
for k=0:255
    
    sum_count = sum_count + counts(k + 1, 1);   % 采用增量法统计求和值
    
    s(1,k+1) = round(255/(M*N)*sum_count);
end


J = s(1,I+1);   % 将原图中的灰度转换为新图像中的灰度级
J = uint8(reshape(J, [M, N]));
