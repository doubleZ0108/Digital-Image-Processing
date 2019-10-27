clear;
clc;

img_path = 'Resources/';
imgs_name = ['hw1_dark_road_1.jpg';'hw1_dark_road_2.jpg';'hw1_dark_road_3.jpg'];
result_path = 'ScreenShots/Global Histogram Equalization/';
[M,N] = size(imgs_name);

for k=1:M
    img_name = imgs_name(k,:);
    I = imread([img_path, img_name]);
    J = myhisteq(I);
    K = histeq(I);
%     figure;
%     subplot(2,2,1); imshow(J);
%     subplot(2,2,2); imhist(J);
%     subplot(2,2,3); imshow(K);
%     subplot(2,2,4); imhist(K);
%     imwrite(J, [result_path, 'myhisteq_',num2str(k),'.png']);
%     imwrite(K, [result_path, 'histeq_',num2str(k),'.png']);
%     figure; imhist(J);
%     figure; imhist(K);
end

function J = myhisteq(I)

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
end

