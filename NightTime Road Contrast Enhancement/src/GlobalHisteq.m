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
% global histogram equalization

[M,N] = size(I);

s = zeros(1, 256);
[counts, pixels] = imhist(I);   % [Number of pixels per pixel | Pixel value (0~255)]

sum_count = 0;
for k=0:255
    
    sum_count = sum_count + counts(k + 1, 1);   % use incremental idea
    
    s(1,k+1) = round(255/(M*N)*sum_count);
end

% convert the grayscale in the original image to the grayscale in the new image
J = s(1,I+1);

% convert the shape to origin shape
J = uint8(reshape(J, [M, N]));

end

