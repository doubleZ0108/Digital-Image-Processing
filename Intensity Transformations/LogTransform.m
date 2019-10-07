clear
clc

I = imread('ScreenShots/Log Transformations/origin.png');

range = getrangefromclass(I);
largest = range(2);
c = largest/log(1+largest);

J = uint8(c*log(double(1+I)));
imwrite(J, 'ScreenShots/LogTramsform/result.png');

