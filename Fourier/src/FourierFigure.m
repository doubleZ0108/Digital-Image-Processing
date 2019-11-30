clc;
clear;

im = imread('../Resources/img.jpg');
im = rgb2gray(im);

imfft = abs(fft2(im));
imfftlog = log10(1 + imfft);

imfftshifted = fftshift(imfftlog);

figure;
imshow(imfftlog, []);
figure;
imshow(imfftshifted, []);
