clear;
clc;

I = imread('ScreenShots/Contrast Stretching/origin2.png');
[width, height,type] = size(I);

x1 = 100; y1 = 30;
x2 = 150; y2 = 100;

J = PieceWiseLineraFunction(I(:,:,1), [x1,y1],[x2,y2]);
J = reshape(J, [width, height]);      % 将运算后得到的矩阵变形成原图片尺寸


%% 函数图像
% figure;
% x = 0:0.1:255;
% y = PieceWiseLineraFunction(x, [x1,y1],[x2,y2]);
% plot(x,y);



function y = PieceWiseLineraFunction(x, p1, p2)
% 分段线性函数
% p1，p2为输入的两点坐标

x1 = p1(1);y1 = p1(2);
x2 = p2(1);y2 = p2(2);


k1 = y1/x1;b1 = 0;
k2 = (y2-y1)/(x2-x1);b2 = y1 - x1*k2;
k3 = (255-y2)/(255-x2);b3 = 255-255*k3;

L1 = x>=0 & x<=x1;
L2 = x>x1 & x<=x2;
L3 = x>x2 & x<=255;
y(L1) = k1.*x(L1)+b1;
y(L2) = k2.*x(L2)+b2;
y(L3) = k3.*x(L3)+b3;

end

