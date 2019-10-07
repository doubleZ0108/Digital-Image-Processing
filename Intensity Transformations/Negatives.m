clear
clc

I = imread('ScreenShots/Negatives/origin.png');
[width, height] = size(I);

%% 直接对每个像素操作（自己写的）

% nagatived_I = zeros(width, height);
% for x=1:width
%     for y=1:height
%         nagatived_I(x,y) = 255 - I(x,y);
%     end
% end


%% 直接进行矩阵运算
negatived_I = 255 - I;
figure;
imshow(negatived_I, []);


%% imcomplement库函数
J = imcomplement(I);
figure;
imshow(J, []);




