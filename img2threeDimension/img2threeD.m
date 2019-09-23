% I = imread('Resources/color.jpg');
I = imread('Resources/gray.jpg');
I = rgb2gray(I);

[height, width] = size(I);  % 注意这里是先高，后宽

xx = 1:1:width;
yy = 1:1:height;
[x,y] = meshgrid(xx,yy);     % 可以适用在长宽不想等的情况下

z = I(:,:,1);

figure;
mesh(x,y,z);