clear
clc

figure;
I = imread('ScreenShots/Gamma Transformations/toobright.png');

gamma = 5;
c = 255/(255^gamma);

J = uint8(c*double(I).^gamma);
