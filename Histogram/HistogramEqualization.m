clc;
clear;

I = imread('Resources/origin2.png');
I = rgb2gray(I);
[M,N] = size(I);

s = zeros(1, 256);
[counts, pixels] = imhist(I);
sum_count = 0;

for k=0:255
    
    sum_count = sum_count + counts(k + 1, 1);
    
    s(1,k+1) = round(255/(M*N)*sum_count);
end


J = s(1,I+1);
J = uint8(reshape(J, [M, N]));
figure;
imhist(I);
hold on;
imhist(J);

figure;
subplot(1,2,1); imshow(I);
subplot(1,2,2); imshow(J);
imwrite(J, 'Resources/result2.png');