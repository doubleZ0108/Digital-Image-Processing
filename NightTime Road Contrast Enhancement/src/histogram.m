clear;
clc;

img_path = 'Resources/';
imgs_name = ['hw1_dark_road_1.jpg';'hw1_dark_road_2.jpg';'hw1_dark_road_3.jpg'];
result_path = 'ScreenShots/Histogram';
[M,N] = size(imgs_name);

for k=1:M
    img_name = imgs_name(k,:);
    I = imread([img_path, img_name]);
    figure;
    imhist(I);
end
