clc;
clear;

I = imread('ScreenShots/Bit Plane/origin.png');
I = rgb2gray(I);

cells = cell(1,8);

for k=1:8
    cells{k} = bitshift(bitget(I, k), k-1);
end



[M,N] = size(I);
J = zeros(M,N,'uint8');
for k=6:8
    J = bitset(J, k, bitget(cells{k}, k));
end
